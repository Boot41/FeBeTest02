import unittest
from unittest.mock import patch
from your_app_path.employee_service import EmployeeService

class TestEmployeeService(unittest.TestCase):
    
    @patch('your_app_path.employee_service.EmployeeService.get_attendance')
    def test_get_attendance_valid(self, mock_get_attendance):
        mock_get_attendance.return_value = {'status': 'success', 'attendance': []}
        response = EmployeeService.get_attendance(1)
        self.assertEqual(response, {'status': 'success', 'attendance': []})

    @patch('your_app_path.employee_service.EmployeeService.get_attendance')
    def test_get_attendance_invalid_employee(self, mock_get_attendance):
        mock_get_attendance.side_effect = Exception('Employee not found')
        with self.assertRaises(Exception) as context:
            EmployeeService.get_attendance(-1)
        self.assertEqual(str(context.exception), 'Employee not found')

    @patch('your_app_path.employee_service.EmployeeService.get_leave_balance')
    def test_get_leave_balance_valid(self, mock_get_leave_balance):
        mock_get_leave_balance.return_value = {'status': 'success', 'leave_balance': 15}
        response = EmployeeService.get_leave_balance(2)
        self.assertEqual(response, {'status': 'success', 'leave_balance': 15})

    @patch('your_app_path.employee_service.EmployeeService.get_leave_balance')
    def test_get_leave_balance_invalid_employee(self, mock_get_leave_balance):
        mock_get_leave_balance.side_effect = Exception('Employee not found')
        with self.assertRaises(Exception) as context:
            EmployeeService.get_leave_balance(-1)
        self.assertEqual(str(context.exception), 'Employee not found')

    @patch('your_app_path.employee_service.EmployeeService.get_recent_activities')
    def test_get_recent_activities_valid(self, mock_get_recent_activities):
        mock_get_recent_activities.return_value = {'status': 'success', 'activities': []}
        response = EmployeeService.get_recent_activities(3)
        self.assertEqual(response, {'status': 'success', 'activities': []})

    @patch('your_app_path.employee_service.EmployeeService.get_recent_activities')
    def test_get_recent_activities_invalid_employee(self, mock_get_recent_activities):
        mock_get_recent_activities.side_effect = Exception('Employee not found')
        with self.assertRaises(Exception) as context:
            EmployeeService.get_recent_activities(-1)
        self.assertEqual(str(context.exception), 'Employee not found')

if __name__ == '__main__':
    unittest.main()