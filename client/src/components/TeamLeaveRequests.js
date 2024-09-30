import React, { useEffect, useState } from 'react';

const TeamLeaveRequests = ({ managerId }) => {
    const [leaveRequests, setLeaveRequests] = useState([]);
    const [error, setError] = useState(null);
    
    // Fetching team leave requests on component mount
    useEffect(() => {
        const fetchLeaveRequests = async () => {
            try {
                const response = await fetch(`http://localhost:8080/api/manager/${managerId}/team-leave-requests`);
                if (!response.ok) throw new Error('Failed to fetch leave requests');
                const data = await response.json();
                setLeaveRequests(data);
            } catch (error) {
                setError(error.message);
            }
        };
        fetchLeaveRequests();
    }, [managerId]);

    // Approve leave request
    const handleApprove = async (requestId) => {
        try {
            const response = await fetch(`http://localhost:8080/api/manager/${managerId}/leave-requests/${requestId}/approve`, {
                method: 'POST',
            });
            if (!response.ok) throw new Error('Failed to approve leave request');
            setLeaveRequests(leaveRequests.filter(request => request.id !== requestId));
        } catch (error) {
            setError(error.message);
        }
    };

    // Deny leave request
    const handleDeny = async (requestId) => {
        try {
            const response = await fetch(`http://localhost:8080/api/manager/${managerId}/leave-requests/${requestId}/deny`, {
                method: 'POST',
            });
            if (!response.ok) throw new Error('Failed to deny leave request');
            setLeaveRequests(leaveRequests.filter(request => request.id !== requestId));
        } catch (error) {
            setError(error.message);
        }
    };

    if (error) return <div className="text-red-500">{error}</div>;

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">Pending Leave Requests</h2>
            <ul className="space-y-3">
                {leaveRequests.length > 0 ? (
                    leaveRequests.map(request => (
                        <li key={request.id} className="border p-3 rounded-lg flex justify-between items-center">
                            <div>
                                <p><strong>{request.employeeName}</strong> - {request.leaveType}</p>
                                <p>{request.startDate} to {request.endDate}</p>
                            </div>
                            <div className="space-x-2">
                                <button 
                                    className="bg-green-500 text-white px-3 py-1 rounded shadow hover:bg-green-600"
                                    onClick={() => handleApprove(request.id)}
                                >
                                    Approve
                                </button>
                                <button 
                                    className="bg-red-500 text-white px-3 py-1 rounded shadow hover:bg-red-600"
                                    onClick={() => handleDeny(request.id)}
                                >
                                    Deny
                                </button>
                            </div>
                        </li>
                    ))
                ) : (
                    <li className="text-gray-500">No pending leave requests.</li>
                )}
            </ul>
        </div>
    );
};

export default TeamLeaveRequests;