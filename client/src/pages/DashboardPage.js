import React, { useEffect, useState } from 'react';
import EmployeeDashboard from '../components/EmployeeDashboard';

const DashboardPage = () => {
    const [attendanceData, setAttendanceData] = useState({});
    const [leaveBalance, setLeaveBalance] = useState({});
    const [recentActivities, setRecentActivities] = useState([]);
    const [error, setError] = useState(null);

    const employeeId = 'YOUR_EMPLOYEE_ID'; // Replace with dynamic employee ID

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

    useEffect(() => {
        fetchAttendance();
        fetchLeaveBalance();
        fetchRecentActivities();
    }, []);

    return (
        <main className="flex flex-col items-center justify-center p-4">
            {error && <div className="alert alert-error">{error}</div>}
            <EmployeeDashboard
                attendanceData={attendanceData}
                leaveBalance={leaveBalance}
                recentActivities={recentActivities}
            />
        </main>
    );
};

export default DashboardPage;