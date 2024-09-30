import React, { useEffect, useState } from 'react'; // Import React and hooks for state and effect
import TeamAttendanceOverview from '../components/TeamAttendanceOverview'; // Import the attendance overview component
import TeamLeaveRequests from '../components/TeamLeaveRequests'; // Import the leave requests component

const MyTeamPage = () => {
    const [attendanceData, setAttendanceData] = useState(null); // State to hold attendance data
    const [leaveRequests, setLeaveRequests] = useState([]); // State to hold leave requests
    const [error, setError] = useState(''); // State to handle errors

    // Fetch attendance data from the API
    const fetchAttendanceData = async (managerId) => {
        try {
            const response = await fetch(`http://localhost:8080/api/manager/${managerId}/team-attendance`); // API call
            if (!response.ok) throw new Error('Failed to fetch attendance data'); // Handle non-200 responses
            const data = await response.json(); // Parse JSON data
            setAttendanceData(data); // Update state with fetched data
        } catch (err) {
            setError(err.message); // Handle errors and update error state
        }
    };

    // Fetch leave requests from the API
    const fetchLeaveRequests = async (managerId) => {
        try {
            const response = await fetch(`http://localhost:8080/api/manager/${managerId}/team-leave-requests`); // API call
            if (!response.ok) throw new Error('Failed to fetch leave requests'); // Handle non-200 responses
            const data = await response.json(); // Parse JSON data
            setLeaveRequests(data); // Update state with fetched data
        } catch (err) {
            setError(err.message); // Handle errors and update error state
        }
    };

    useEffect(() => {
        const managerId = '123'; // Replace with dynamic manager ID as needed
        fetchAttendanceData(managerId); // Call function to fetch attendance data on component mount
        fetchLeaveRequests(managerId); // Call function to fetch leave requests on component mount
    }, []); // Empty dependency array means this runs once on mount

    return (
        <div className="p-4 md:p-6 lg:p-8">
            {error && <div className="text-red-500">{error}</div>} // Display error message if any
            {attendanceData ? ( // Conditional rendering based on data availability
                <>
                    <TeamAttendanceOverview data={attendanceData} /> // Attendance overview component with data
                    <TeamLeaveRequests requests={leaveRequests} /> // Leave requests component with data
                </>
            ) : (
                <div className="flex justify-center items-center h-full">
                    <p>Loading attendance data...</p> // Loading state 
                </div>
            )}
        </div>
    );
};

export default MyTeamPage; // Export the component for use in the application.