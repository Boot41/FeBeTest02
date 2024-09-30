import React, { useEffect, useState } from 'react';

const OrganizationDirectory = () => {
    const [employees, setEmployees] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchEmployees = async () => {
            try {
                const response = await fetch('http://localhost:8080/api/organization/directory');
                if (!response.ok) {
                    throw new Error('Network response was not ok' + response.statusText);
                }
                const data = await response.json();
                setEmployees(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchEmployees();
    }, []);

    if (loading) return <div className="text-center">Loading...</div>;
    if (error) return <div className="text-red-500">{error}</div>;

    return (
        <div className="overflow-x-auto">
            <table className="min-w-full bg-white dark:bg-gray-800">
                <thead className="bg-gray-200 dark:bg-gray-700">
                    <tr>
                        <th className="py-2 px-4 text-left">Name</th>
                        <th className="py-2 px-4 text-left">Position</th>
                        <th className="py-2 px-4 text-left">Department</th>
                    </tr>
                </thead>
                <tbody>
                    {employees.map((employee) => (
                        <tr key={employee.id} className="border-t dark:border-gray-600">
                            <td className="py-2 px-4">{employee.name}</td>
                            <td className="py-2 px-4">{employee.position}</td>
                            <td className="py-2 px-4">{employee.department}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default OrganizationDirectory;