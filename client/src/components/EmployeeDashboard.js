import React, { useEffect, useState } from 'react';

// EmployeeDashboard component to display widgets for attendance stats, leave balance, and recent activities
const EmployeeDashboard = ({ employeeId }) => {
    const [attendanceData, setAttendanceData] = useState(null);
    const [leaveBalance, setLeaveBalance] = useState(null);
    const [recentActivities, setRecentActivities] = useState([]);
    const [error, setError] = useState(null);

    // Fetch attendance data
    const fetchAttendance = async () => {
        try {
            const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/attendance`);
            if (!response.ok) throw new Error('Failed to fetch attendance data');
            const data = await response.json();
            setAttendanceData(data);
        } catch (err) {
            setError(err.message);
        }
    };

    // Fetch leave balance
    const fetchLeaveBalance = async () => {
        try {
            const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/leave-balance`);
            if (!response.ok) throw new Error('Failed to fetch leave balance');
            const data = await response.json();
            setLeaveBalance(data);
        } catch (err) {
            setError(err.message);
        }
    };

    // Fetch recent activities
    const fetchRecentActivities = async () => {
        try {
            const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/recent-activities`);
            if (!response.ok) throw new Error('Failed to fetch recent activities');
            const data = await response.json();
            setRecentActivities(data);
        } catch (err) {
            setError(err.message);
        }
    };

    // Use useEffect to fetch data on component mount
    useEffect(() => {
        fetchAttendance();
        fetchLeaveBalance();
        fetchRecentActivities();
    }, [employeeId]);

    return (
        <div className="p-4 space-y-6">
            {error && <div className="text-red-500">{error}</div>}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-white shadow-lg rounded-lg p-4">
                    <h2 className="text-lg font-semibold">Attendance</h2>
                    {attendanceData ? (
                        <div>{attendanceData.status} - {attendanceData.daysPresent} days present</div>
                    ) : (
                        <div>Loading...</div>
                    )}
                </div>
                <div className="bg-white shadow-lg rounded-lg p-4">
                    <h2 className="text-lg font-semibold">Leave Balance</h2>
                    {leaveBalance ? (
                        <div>{leaveBalance.daysRemaining} days remaining</div>
                    ) : (
                        <div>Loading...</div>
                    )}
                </div>
                <div className="bg-white shadow-lg rounded-lg p-4">
                    <h2 className="text-lg font-semibold">Recent Activities</h2>
                    {recentActivities.length > 0 ? (
                        <ul>
                            {recentActivities.map(activity => (
                                <li key={activity.id}>{activity.description} - {activity.date}</li>
                            ))}
                        </ul>
                    ) : (
                        <div>No recent activities</div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default EmployeeDashboard;