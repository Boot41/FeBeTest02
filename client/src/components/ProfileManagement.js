import React, { useEffect, useState } from 'react';

const ProfileManagement = () => {
    const [profileData, setProfileData] = useState({
        name: '',
        email: '',
        contact_number: '',
        address: '',
    });
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(true);

    const employeeId = 1; // retrieve the employee ID based on authentication context

    useEffect(() => {
        fetch(`http://localhost:8080/api/employee/${employeeId}/profile`)
            .then(response => response.json())
            .then(data => {
                setProfileData(data);
                setIsLoading(false);
            })
            .catch(err => {
                setError('Failed to load profile data.');
                setIsLoading(false);
            });
    }, [employeeId]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setProfileData(prevData => ({ ...prevData, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch(`http://localhost:8080/api/employee/${employeeId}/profile/update`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(profileData),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(() => {
                alert('Profile updated successfully!');
            })
            .catch(err => {
                setError('Failed to update profile.');
            });
    };

    if (isLoading) return <div>Loading...</div>;

    return (
        <div className="p-4 bg-gray-800 rounded-lg shadow-md">
            <h2 className="text-xl font-bold text-white mb-4">Profile Management</h2>
            {error && <p className="text-red-500">{error}</p>}
            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label className="block text-white">Name:</label>
                    <input
                        type="text"
                        name="name"
                        value={profileData.name}
                        onChange={handleChange}
                        className="w-full p-2 rounded-lg border border-gray-300 focus:outline-none focus:ring focus:ring-orange-500"
                        required
                    />
                </div>
                <div>
                    <label className="block text-white">Email:</label>
                    <input
                        type="email"
                        name="email"
                        value={profileData.email}
                        onChange={handleChange}
                        className="w-full p-2 rounded-lg border border-gray-300 focus:outline-none focus:ring focus:ring-orange-500"
                        required
                    />
                </div>
                <div>
                    <label className="block text-white">Contact Number:</label>
                    <input
                        type="tel"
                        name="contact_number"
                        value={profileData.contact_number}
                        onChange={handleChange}
                        className="w-full p-2 rounded-lg border border-gray-300 focus:outline-none focus:ring focus:ring-orange-500"
                        required
                    />
                </div>
                <div>
                    <label className="block text-white">Address:</label>
                    <textarea
                        name="address"
                        value={profileData.address}
                        onChange={handleChange}
                        className="w-full p-2 rounded-lg border border-gray-300 focus:outline-none focus:ring focus:ring-orange-500"
                        required
                    />
                </div>
                <button
                    type="submit"
                    className="w-full p-2 bg-blue-600 text-white rounded-lg hover:bg-blue-500 transition duration-200"
                >
                    Update Profile
                </button>
            </form>
        </div>
    );
};

export default ProfileManagement;