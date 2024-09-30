import React, { useEffect, useState } from 'react';

const CalendarIntegration = ({ employeeId }) => {
    const [calendarProvider, setCalendarProvider] = useState('');
    const [credentials, setCredentials] = useState('');
    const [events, setEvents] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const linkCalendar = async () => {
        setLoading(true);
        setError(null);

        try {
            const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/calendar/link`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ calendar_provider: calendarProvider, credentials }),
            });

            if (!response.ok) throw new Error('Failed to link calendar');

            setCredentials('');
            // Optionally refetch events after linking
            fetchEvents();
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const fetchEvents = async () => {
        setLoading(true);
        setError(null);

        try {
            const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/calendar/events`, {
                method: 'GET',
            });

            if (!response.ok) throw new Error('Failed to fetch events');

            const data = await response.json();
            setEvents(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchEvents();
    }, []);

    return (
        <div className="p-4 bg-gray-800 text-white rounded-lg shadow-lg">
            <h2 className="text-xl font-bold mb-4">Calendar Integration</h2>
            <div className="mb-4">
                <label className="block mb-2">Calendar Provider:</label>
                <input
                    type="text"
                    value={calendarProvider}
                    onChange={(e) => setCalendarProvider(e.target.value)}
                    className="w-full p-2 border border-gray-600 rounded focus:outline-none focus:ring focus:ring-blue-500"
                />
                <label className="block mb-2 mt-4">Credentials:</label>
                <input
                    type="text"
                    value={credentials}
                    onChange={(e) => setCredentials(e.target.value)}
                    className="w-full p-2 border border-gray-600 rounded focus:outline-none focus:ring focus:ring-blue-500"
                />
                <button
                    onClick={linkCalendar}
                    className="mt-4 bg-blue-500 text-white p-2 rounded hover:bg-blue-600 transition"
                    disabled={loading}
                >
                    {loading ? 'Linking...' : 'Link Calendar'}
                </button>
            </div>
            {error && <p className="text-red-500 mb-4">{error}</p>}
            <h3 className="text-lg font-semibold">Upcoming Events</h3>
            <ul className="list-disc pl-6">
                {events.map((event) => (
                    <li key={event.id} className="my-2">
                        {event.title} - {new Date(event.start).toLocaleString()}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CalendarIntegration;