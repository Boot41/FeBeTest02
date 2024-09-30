from django.test import TestCase
from .models import Employee, Attendance, LeaveBalance, RecentActivity, LeaveRequest, Organization, EmployeeDirectory, HierarchicalStructure, EmployeeProfile, AttendanceReport, Notification, Role, EmployeeRole

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

    def test_leave_request_empty_reason(self):
        leave_request = LeaveRequest.objects.create(employee=self.employee, leave_type='Vacation', start_date='2023-10-05', end_date='2023-10-10', reason='')
        self.assertEqual(leave_request.reason, '')

    def test_leave_request_with_long_reason(self):
        long_reason = 'a' * 256
        with self.assertRaises(ValueError):
            LeaveRequest.objects.create(employee=self.employee, leave_type='Vacation', start_date='2023-10-05', end_date='2023-10-10', reason=long_reason)

    def test_leave_request_status_update(self):
        self.leave_request.status = 'approved'
        self.leave_request.save()
        self.assertEqual(self.leave_request.status, 'approved')

class OrganizationModelTest(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(name='Tech Corp')

    def test_organization_creation(self):
        self.assertEqual(self.organization.name, 'Tech Corp')

class EmployeeDirectoryModelTest(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(name='Tech Corp')
        self.employee = Employee.objects.create(name='John Doe')
        self.employee_directory = EmployeeDirectory.objects.create(employee=self.employee, organization=self.organization)

    def test_employee_directory_creation(self):
        self.assertEqual(self.employee_directory.employee, self.employee)
        self.assertEqual(self.employee_directory.organization, self.organization)

class HierarchicalStructureModelTest(TestCase):
    def setUp(self):
        self.manager = Employee.objects.create(name='Manager Doe')
        self.subordinate = Employee.objects.create(name='Subordinate Doe')
        self.hierarchy = HierarchicalStructure.objects.create(employee=self.subordinate, manager=self.manager)

    def test_hierarchical_structure_creation(self):
        self.assertEqual(self.hierarchy.employee, self.subordinate)
        self.assertEqual(self.hierarchy.manager, self.manager)

class EmployeeProfileModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='Alice Jones')
        self.employee_profile = EmployeeProfile.objects.create(employee=self.employee, phone_number='1234567890', address='123 Main St', date_of_birth='1990-01-01', position='Developer')

    def test_employee_profile_creation(self):
        self.assertEqual(self.employee_profile.employee, self.employee)
        self.assertEqual(self.employee_profile.phone_number, '1234567890')
        self.assertEqual(self.employee_profile.address, '123 Main St')
        self.assertEqual(self.employee_profile.date_of_birth, '1990-01-01')
        self.assertEqual(self.employee_profile.position, 'Developer')

    def test_employee_profile_no_employee(self):
        with self.assertRaises(ValueError):
            EmployeeProfile.objects.create(employee=None, phone_number='1234567890')

class AttendanceReportModelTest(TestCase):
    def setUp(self):
        self.manager = Employee.objects.create(name='Manager Lee')
        self.attendance_report = AttendanceReport.objects.create(manager=self.manager, date_range_start='2023-10-01', date_range_end='2023-10-31', attendance_data={'present': 20, 'absent': 5})

    def test_attendance_report_creation(self):
        self.assertEqual(self.attendance_report.manager, self.manager)
        self.assertEqual(self.attendance_report.date_range_start, '2023-10-01')
        self.assertEqual(self.attendance_report.date_range_end, '2023-10-31')
        self.assertEqual(self.attendance_report.attendance_data, {'present': 20, 'absent': 5})

    def test_attendance_report_no_manager(self):
        with self.assertRaises(ValueError):
            AttendanceReport.objects.create(manager=None, date_range_start='2023-10-01', date_range_end='2023-10-31', attendance_data={})

class NotificationModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='Sam Green')
        self.notification = Notification.objects.create(employee=self.employee, message='You have a new message')

    def test_notification_creation(self):
        self.assertEqual(self.notification.message, 'You have a new message')
        self.assertEqual(self.notification.is_read, False)
        self.assertIsNotNone(self.notification.timestamp)

    def test_notification_foreign_key(self):
        self.assertEqual(self.notification.employee, self.employee)

    def test_notification_empty_message(self):
        with self.assertRaises(ValueError):
            Notification.objects.create(employee=self.employee, message='')

class RoleModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name='Admin', permissions={'read': True, 'write': True})

    def test_role_creation(self):
        self.assertEqual(self.role.name, 'Admin')
        self.assertEqual(self.role.permissions, {'read': True, 'write': True})

class EmployeeRoleModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name='User', permissions={'read': True})
        self.employee = Employee.objects.create(name='Tom Brown')
        self.employee_role = EmployeeRole.objects.create(employee=self.employee, role=self.role)

    def test_employee_role_creation(self):
        self.assertEqual(self.employee_role.employee, self.employee)
        self.assertEqual(self.employee_role.role, self.role)

    def test_employee_role_foreign_key(self):
        self.assertEqual(self.employee_role.employee, self.employee)
        self.assertEqual(self.employee_role.role, self.role)