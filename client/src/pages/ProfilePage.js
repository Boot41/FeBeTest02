import React, { useState, useEffect } from 'react'; // Import React and hooks
import ProfileManagement from '../components/ProfileManagement'; // Import the ProfileManagement component

const ProfilePage = () => {
    // Define state to handle employee profile data
    const [profileData, setProfileData] = useState(null); 
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
        </div>
    );
};

export default ProfilePage; // Export the ProfilePage component