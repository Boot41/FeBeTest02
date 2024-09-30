import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2'; // Using chart library for visual representations
import 'chart.js/auto'; // Automatic registration of chart components

const AttendanceReport = ({ managerId }) => {
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [attendanceData, setAttendanceData] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const fetchAttendanceData = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await fetch(`http://localhost:8080/api/manager/${managerId}/attendance-reports?start_date=${startDate}&end_date=${endDate}`);
            if (!response.ok) throw new Error('Failed to fetch data');
            const data = await response.json();
            setAttendanceData(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (startDate && endDate) {
            fetchAttendanceData();
        }
    };

    // Chart data preparation
    const chartData = {
        labels: attendanceData ? attendanceData.map(item => item.date) : [],
        datasets: [
            {
                label: 'Attendance',
                data: attendanceData ? attendanceData.map(item => item.count) : [],
                fill: false,
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1)',
            }
        ]
    };

    return (
        <div className="p-4 bg-gray-800 text-white rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-4">Attendance Report</h2>
            <form onSubmit={handleSubmit} className="flex flex-col md:flex-row mb-4">
                <input 
                    type="date" 
                    value={startDate} 
                    onChange={(e) => setStartDate(e.target.value)} 
                    className="p-2 mr-2 border border-gray-400 rounded-md focus:outline-none focus:ring focus:ring-blue-500" 
                    aria-label="Start Date"
                    required 
                />
                <input 
                    type="date" 
                    value={endDate} 
                    onChange={(e) => setEndDate(e.target.value)} 
                    className="p-2 mr-2 border border-gray-400 rounded-md focus:outline-none focus:ring focus:ring-blue-500" 
                    aria-label="End Date"
                    required 
                />
                <button 
                    type="submit" 
                    className="p-2 bg-blue-600 rounded-md text-white hover:bg-blue-700 transition duration-200" 
                    aria-label="Generate Report"
                >
                    Generate
                </button>
            </form>

            {error && <div className="text-red-500">{error}</div>}
            {loading && <div>Loading...</div>}

            {attendanceData && (
                <div className="mt-4">
                    <Line data={chartData} />
                </div>
            )}
        </div>
    );
};

export default AttendanceReport;