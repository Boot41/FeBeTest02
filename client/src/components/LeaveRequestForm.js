import React, { useState } from 'react';

const LeaveRequestForm = () => {
    const [leaveType, setLeaveType] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [reason, setReason] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setSuccess('');

        if (!leaveType || !startDate || !endDate || !reason) {
            setError('All fields are required.');
            return;
        }

        try {
            const response = await fetch('/api/employee/{employee_id}/request-leave', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ leave_type: leaveType, start_date: startDate, end_date: endDate, reason }),
            });

            if (!response.ok) throw new Error('Network response was not ok');

            const data = await response.json();
            if (data.success) {
                setSuccess('Leave request submitted successfully!');
                // Reset form after successful submission
                setLeaveType('');
                setStartDate('');
                setEndDate('');
                setReason('');
            } else {
                setError(data.message || 'Failed to submit leave request.');
            }
        } catch (err) {
            setError(err.message || 'An error occurred');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="max-w-md mx-auto p-4 bg-white rounded shadow-md space-y-4">
            <h2 className="text-lg font-semibold">Leave Request Form</h2>
            {error && <p className="text-red-500">{error}</p>}
            {success && <p className="text-green-500">{success}</p>}

            <label className="block">
                <span className="text-gray-700">Leave Type</span>
                <select 
                    value={leaveType} 
                    onChange={(e) => setLeaveType(e.target.value)} 
                    className="mt-1 block w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                    required
                >
                    <option value="">Select leave type</option>
                    <option value="sick">Sick Leave</option>
                    <option value="vacation">Vacation</option>
                    <option value="personal">Personal Leave</option>
                </select>
            </label>

            <label className="block">
                <span className="text-gray-700">Start Date</span>
                <input 
                    type="date" 
                    value={startDate} 
                    onChange={(e) => setStartDate(e.target.value)} 
                    className="mt-1 block w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                    required
                />
            </label>

            <label className="block">
                <span className="text-gray-700">End Date</span>
                <input 
                    type="date" 
                    value={endDate} 
                    onChange={(e) => setEndDate(e.target.value)} 
                    className="mt-1 block w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                    required
                />
            </label>

            <label className="block">
                <span className="text-gray-700">Reason</span>
                <textarea 
                    value={reason} 
                    onChange={(e) => setReason(e.target.value)} 
                    className="mt-1 block w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                    rows="4"
                    required
                ></textarea>
            </label>

            <button 
                type="submit" 
                className="w-full bg-blue-500 text-white rounded p-2 hover:bg-blue-600 transition ease-in-out duration-150"
            >
                Submit Leave Request
            </button>
        </form>
    );
};

export default LeaveRequestForm;