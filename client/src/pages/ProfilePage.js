import React, { useState, useEffect } from 'react'; // Import React and hooks
import ProfileManagement from '../components/ProfileManagement'; // Import the ProfileManagement component
import CalendarIntegration from '../components/CalendarIntegration'; // Import the CalendarIntegration component

const ProfilePage = () => {
    // Define state to handle employee profile data and calendar events
    const [profileData, setProfileData] = useState(null); 
    const [calendarEvents, setCalendarEvents] = useState([]); 
    const [error, setError] = useState(null); 
    const employeeId = 1; // Sample employee ID, replace as necessary

    // Fetch profile data from API on component mount
    useEffect(() => {
        const fetchProfileData = async () => {
            try {
                const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/profile`);
                if (!response.ok) throw new Error('Failed to fetch profile data');
                const data = await response.json();
                setProfileData(data);
            } catch (err) {
                setError(err.message);
            }
        };

        fetchProfileData();
    }, [employeeId]);

    // Fetch calendar events based on the employee's calendar
    useEffect(() => {
        const fetchCalendarEvents = async () => {
            const today = new Date();
            const startDate = today.toISOString().split('T')[0]; // Get today's date
            const endDate = new Date(today);
            endDate.setMonth(today.getMonth() + 1); // Get one month later
            const endDateString = endDate.toISOString().split('T')[0]; // Get the end date

            try {
                const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/calendar/events?start_date=${startDate}&end_date=${endDateString}`);
                if (!response.ok) throw new Error('Failed to fetch calendar events');
                const eventsData = await response.json();
                setCalendarEvents(eventsData);
            } catch (err) {
                setError(err.message);
            }
        };

        fetchCalendarEvents();
    }, [employeeId]);

    // Error handling section
    if (error) {
        return <div className="text-red-500">{error}</div>; // Show error message
    }

    // Render loading state while fetching data
    if (!profileData) {
        return <div className="text-gray-500">Loading...</div>; 
    }

    // Render the ProfileManagement component with fetched data
    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Profile Management</h1>
            <ProfileManagement profileData={profileData} employeeId={employeeId} />
            <CalendarIntegration events={calendarEvents} employeeId={employeeId} /> {/* Calendar Integration Component */}
        </div>
    );
};

export default ProfilePage; // Export the ProfilePage component.