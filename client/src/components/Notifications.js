import React, { useEffect, useState } from 'react';

const Notifications = ({ employeeId }) => {
  const [notifications, setNotifications] = useState([]);
  const [error, setError] = useState(null);

  // Fetch notifications from the API
  const fetchNotifications = async () => {
    try {
      const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/notifications`);
      if (!response.ok) {
        throw new Error('Failed to fetch notifications');
      }
      const data = await response.json();
      setNotifications(data);
    } catch (err) {
      setError(err.message);
    }
  };

  // Mark notification as read
  const markAsRead = async (notificationId) => {
    try {
      const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/notifications/${notificationId}/read`, {
        method: 'POST',
      });
      if (!response.ok) {
        throw new Error('Failed to mark notification as read');
      }
      // Update notifications state to remove the read notification
      setNotifications((prev) => prev.filter((notif) => notif.id !== notificationId));
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
    fetchNotifications();
  }, [employeeId]);

  return (
    <div className="relative">
      <button className="bg-gray-700 text-white py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-orange-500">
        Notifications
      </button>
      <div className="absolute right-0 mt-2 w-64 rounded-lg shadow-lg bg-white z-10">
        {error && <div className="p-4 text-red-500">{error}</div>}
        <ul>
          {notifications.map((notif) => (
            <li key={notif.id} className="flex justify-between p-4 border-b hover:bg-gray-100">
              <div>
                <p className="font-semibold">{notif.title}</p>
                <p className="text-sm text-gray-600">{notif.message}</p>
              </div>
              <button
                onClick={() => markAsRead(notif.id)}
                className="text-blue-500 hover:underline"
                aria-label={`Mark notification ${notif.title} as read`}
              >
                Dismiss
              </button>
            </li>
          ))}
        </ul>
        {notifications.length === 0 && <div className="p-4 text-center text-gray-500">No notifications</div>}
      </div>
    </div>
  );
};

export default Notifications;