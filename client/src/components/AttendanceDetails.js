import React, { useEffect, useState } from 'react';

const AttendanceDetails = () => {
    const [attendanceRecords, setAttendanceRecords] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    const employeeId = 1; // Replace with dynamic employee ID as needed

    useEffect(() => {
        const fetchAttendanceDetails = async () => {
            try {
                const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/attendance-details`);
                if (!response.ok) throw new Error('Failed to fetch attendance details');
                const data = await response.json();
                setAttendanceRecords(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };
        
        fetchAttendanceDetails();
    }, [employeeId]);

    if (loading) return <div className="text-center">Loading attendance records...</div>;
    if (error) return <div className="text-red-500 text-center">{error}</div>;

    return (
        <div className="p-4">
            <h2 className="text-2xl font-bold mb-4">Attendance Details</h2>
            <table className="min-w-full border-collapse border border-gray-200">
                <thead>
                    <tr>
                        <th className="border border-gray-200 px-4 py-2">Date</th>
                        <th className="border border-gray-200 px-4 py-2">Check-in</th>
                        <th className="border border-gray-200 px-4 py-2">Check-out</th>
                        <th className="border border-gray-200 px-4 py-2">Total Hours Worked</th>
                    </tr>
                </thead>
                <tbody>
                    {attendanceRecords.map((record) => (
                        <tr key={record.date}>
                            <td className="border border-gray-200 px-4 py-2">{record.date}</td>
                            <td className="border border-gray-200 px-4 py-2">{record.checkIn}</td>
                            <td className="border border-gray-200 px-4 py-2">{record.checkOut}</td>
                            <td className="border border-gray-200 px-4 py-2">{record.totalHours}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default AttendanceDetails;