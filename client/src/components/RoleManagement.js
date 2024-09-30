import React, { useEffect, useState } from 'react';

// RoleManagement component for managing roles and permissions
const RoleManagement = () => {
    const [roles, setRoles] = useState([]); // State for storing roles
    const [newRole, setNewRole] = useState({ role_name: '', permissions: [] }); // State for new role input
    const [error, setError] = useState(''); // State for error messages

    // Fetch existing roles from API
    useEffect(() => {
        const fetchRoles = async () => {
            try {
                const response = await fetch('/api/hr/roles');
                if (!response.ok) throw new Error('Failed to fetch roles');
                const data = await response.json();
                setRoles(data);
            } catch (err) {
                setError(err.message);
            }
        };
        fetchRoles();
    }, []);

    // Handle creating a new role
    const handleCreateRole = async () => {
        try {
            const response = await fetch('/api/hr/roles/create', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(newRole),
            });
            if (!response.ok) throw new Error('Failed to create role');
            const data = await response.json();
            setRoles([...roles, data]);
            setNewRole({ role_name: '', permissions: [] });
        } catch (err) {
            setError(err.message);
        }
    };

    // Handle updating a role
    const handleUpdateRole = async (roleId) => {
        try {
            const response = await fetch(`/api/hr/roles/${roleId}/update`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ permissions: roles.find(role => role.id === roleId).permissions }),
            });
            if (!response.ok) throw new Error('Failed to update role');
            // Update local roles state if necessary
        } catch (err) {
            setError(err.message);
        }
    };

    // Handle deleting a role
    const handleDeleteRole = async (roleId) => {
        try {
            const response = await fetch(`/api/hr/roles/${roleId}/delete`, {
                method: 'DELETE',
            });
            if (!response.ok) throw new Error('Failed to delete role');
            setRoles(roles.filter(role => role.id !== roleId));
        } catch (err) {
            setError(err.message);
        }
    };

    return (
        <div className="p-4">
            <h2 className="text-2xl font-bold mb-4">Role Management</h2>
            {error && <p className="text-red-500">{error}</p>}
            <div className="mb-4">
                <input
                    type="text"
                    value={newRole.role_name}
                    onChange={(e) => setNewRole({ ...newRole, role_name: e.target.value })}
                    placeholder="Role Name"
                    className="border rounded p-2 mr-2"
                />
                <button onClick={handleCreateRole} className="bg-blue-500 text-white p-2 rounded">Add Role</button>
            </div>
            <ul>
                {roles.map(role => (
                    <li key={role.id} className="flex justify-between items-center mb-2">
                        <input
                            type="text"
                            value={role.role_name}
                            onChange={(e) => {
                                const updatedRoles = roles.map(r => r.id === role.id ? { ...r, role_name: e.target.value } : r);
                                setRoles(updatedRoles);
                            }}
                            className="border rounded p-2 mr-2 flex-1"
                        />
                        <button onClick={() => handleUpdateRole(role.id)} className="bg-green-500 text-white p-2 rounded">Update</button>
                        <button onClick={() => handleDeleteRole(role.id)} className="bg-red-500 text-white p-2 rounded ml-2">Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default RoleManagement;