import React, { useEffect, useState } from 'react';

// OrgStructure Component to visualize the hierarchy of the organization
const OrgStructure = () => {
    // State to hold the organization structure
    const [orgStructure, setOrgStructure] = useState([]);
    const [error, setError] = useState(null);

    // Fetch organization structure data from API
    const fetchOrgStructure = async () => {
        try {
            const response = await fetch('http://localhost:8080/api/organization/structure');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            setOrgStructure(data);
        } catch (error) {
            setError(error.message);
        }
    };

    useEffect(() => {
        fetchOrgStructure();
    }, []);

    // Render error message if any
    if (error) {
        return <div className="text-red-500">{error}</div>;
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">Organization Structure</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {orgStructure.map((department) => (
                    <div key={department.id} className="bg-white shadow-lg rounded-lg p-4">
                        <h3 className="text-lg font-semibold">{department.name}</h3>
                        <ul className="list-disc list-inside">
                            {department.roles.map((role) => (
                                <li key={role.id} className="mt-1">{role.title}</li>
                            ))}
                        </ul>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default OrgStructure;