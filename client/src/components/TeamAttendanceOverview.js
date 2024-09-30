import React, { useEffect, useState } from 'react';
import Chart from 'react-apexcharts'; // Assuming using ApexCharts
import { useParams } from 'react-router-dom';

const TeamAttendanceOverview = () => {
    const { manager_id } = useParams();
    const [attendanceData, setAttendanceData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAttendanceData = async () => {
            try {
                const response = await fetch(`http://localhost:8080/api/manager/${manager_id}/team-attendance`);
                if (!response.ok) throw new Error('Failed to fetch data');
                const data = await response.json();
                setAttendanceData(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };
        
        fetchAttendanceData();
    }, [manager_id]);

    if (loading) return <div className="text-center">Loading...</div>;
    if (error) return <div className="text-red-500">{error}</div>;

    const chartOptions = {
        chart: {
            id: 'attendance-chart',
            toolbar: { show: false },
        },
        xaxis: {
            categories: attendanceData.map(member => member.name), // or appropriate keys
        },
    };

    const chartSeries = [
        {
            name: 'Attendance',
            data: attendanceData.map(member => member.attendance_percentage), // or appropriate keys
        },
    ];

    return (
        <div className="p-5">
            <h2 className="text-lg font-semibold mb-4">Team Attendance Overview</h2>
            <div className="bg-white rounded-lg shadow-md p-4">
                <Chart options={chartOptions} series={chartSeries} type="bar" height={300} />
            </div>
        </div>
    );
}

export default TeamAttendanceOverview;