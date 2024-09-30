import React, { useEffect, useState } from 'react'; // Importing React and hooks
import OrganizationDirectory from '../components/OrganizationDirectory'; // Importing the OrganizationDirectory component
import OrgStructure from '../components/OrgStructure'; // Importing the OrgStructure component
import RoleManagement from '../components/RoleManagement'; // Importing the RoleManagement component

const OrganizationPage = () => {
    const [employees, setEmployees] = useState([]); // State to store employee data
    const [roles, setRoles] = useState([]); // State to store role data
    const [error, setError] = useState(null); // State to store error messages

    // Function to fetch employee data from API
    const fetchEmployees = async () => {
        try {
            const response = await fetch('http://localhost:8080/api/organization/directory'); // Fetching data from the API
            if (!response.ok) {
                throw new Error('Network response was not ok'); // Throw error if response is not okay
            }
            const data = await response.json(); // Converting response to JSON
            setEmployees(data); // Updating state with employee data
        } catch (error) {
            setError(error.message); // Setting error state
        }
    };

    // Function to fetch role data from API
    const fetchRoles = async () => {
        try {
            const response = await fetch('http://localhost:8080/api/hr/roles'); // Fetching roles from API
            if (!response.ok) {
                throw new Error('Failed to fetch roles'); // Throw error if fetching roles fails
            }
            const data = await response.json(); // Converting response to JSON
            setRoles(data); // Updating state with role data
        } catch (error) {
            setError(error.message); // Setting error state
        }
    };

    // Fetch employees and roles on component mount
    useEffect(() => {
        fetchEmployees(); // Fetching employee data on component mount
        fetchRoles(); // Fetching role data on component mount
    }, []); // Empty dependency array to run only on mount

    return (
        <main className="flex flex-col p-6 space-y-4 min-h-screen"> {/* Main content area with padding and spacing */}
            {error && <p className="text-red-500">{error}</p>} {/* Displaying error message if there is an error */}
            <h1 className="text-3xl font-bold">Organization Overview</h1> {/* Main title */}
            <OrganizationDirectory employees={employees} /> {/* Rendering OrganizationDirectory component and passing employee data */}
            <OrgStructure /> {/* Rendering OrgStructure component */}
            <RoleManagement roles={roles} /> {/* Rendering RoleManagement component and passing role data */}
        </main>
    );
};

export default OrganizationPage; // Exporting OrganizationPage component