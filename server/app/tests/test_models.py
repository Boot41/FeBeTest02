from django.test import TestCase
from .models import Employee, Attendance, LeaveBalance, RecentActivity, LeaveRequest

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='John Doe')

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, 'John Doe')
        self.assertIsInstance(self.employee.employee_id, int)

class AttendanceModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='John Doe')
        self.attendance = Attendance.objects.create(employee=self.employee, date='2023-10-01', status='Present')

    def test_attendance_creation(self):
        self.assertEqual(self.attendance.status, 'Present')
        self.assertEqual(self.attendance.date, '2023-10-01')

    def test_attendance_foreign_key(self):
        self.assertEqual(self.attendance.employee, self.employee)

class LeaveBalanceModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='Jane Doe')
        self.leave_balance = LeaveBalance.objects.create(employee=self.employee, leave_type='Sick', balance=10)

    def test_leave_balance_creation(self):
        self.assertEqual(self.leave_balance.leave_type, 'Sick')
        self.assertEqual(self.leave_balance.balance, 10)

    def test_leave_balance_foreign_key(self):
        self.assertEqual(self.leave_balance.employee, self.employee)

class RecentActivityModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='Jake Doe')
        self.activity = RecentActivity.objects.create(employee=self.employee, activity='Logged in')

    def test_recent_activity_creation(self):
        self.assertEqual(self.activity.activity, 'Logged in')
        self.assertIsNotNone(self.activity.timestamp)

    def test_recent_activity_foreign_key(self):
        self.assertEqual(self.activity.employee, self.employee)

class LeaveRequestModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='Jane Smith')
        self.leave_request = LeaveRequest.objects.create(employee=self.employee, leave_type='Vacation', start_date='2023-10-05', end_date='2023-10-10')

    def test_leave_request_creation(self):
        self.assertEqual(self.leave_request.leave_type, 'Vacation')
        self.assertEqual(self.leave_request.status, 'pending')
        self.assertEqual(self.leave_request.start_date, '2023-10-05')
        self.assertEqual(self.leave_request.end_date, '2023-10-10')

    def test_leave_request_foreign_key(self):
        self.assertEqual(self.leave_request.employee, self.employee)

    def test_leave_request_invalid_dates(self):
        with self.assertRaises(ValueError):
            LeaveRequest.objects.create(employee=self.employee, leave_type='Vacation', start_date='2023-10-10', end_date='2023-10-05')

    def test_leave_request_no_employee(self):
        with self.assertRaises(ValueError):
            LeaveRequest.objects.create(employee=None, leave_type='Vacation', start_date='2023-10-05', end_date='2023-10-10')
