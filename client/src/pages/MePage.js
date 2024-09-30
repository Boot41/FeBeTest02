import React, { useEffect, useState } from 'react'; // Import React and hooks
import AttendanceDetails from '../components/AttendanceDetails'; // Import AttendanceDetails component
import LeaveRequestForm from '../components/LeaveRequestForm'; // Import LeaveRequestForm component

const MePage = () => {
  const [attendanceData, setAttendanceData] = useState([]); // State for attendance data
  const [error, setError] = useState(null); // State for error handling
  const employeeId = 1; // Placeholder for employee ID; replace with dynamic value as needed

  // Fetch attendance details from API
  const fetchAttendanceDetails = async () => {
    try {
      const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/attendance-details`);
      if (!response.ok) {
        throw new Error('Network response was not ok'); // Handle network errors
      }
      const data = await response.json();
      setAttendanceData(data); // Set attendance data in state
    } catch (error) {
      setError(error.message); // Set error message in state
    }
  };

  useEffect(() => {
    fetchAttendanceDetails(); // Call fetch function on component mount
  }, []);

  return (
    <div className="container mx-auto p-4"> {/* Responsive container for the main content */}
      <h1 className="text-2xl font-bold mb-4">My Attendance Records</h1> {/* Page title */}
      
      {error && <p className="text-red-500 mb-4">{error}</p>} {/* Error message display */}

      <AttendanceDetails records={attendanceData} /> {/* Attendance details component */}
      <LeaveRequestForm /> {/* Leave request form component */}
    </div>
  );
};

export default MePage; // Export the MePage component