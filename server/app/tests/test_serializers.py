from rest_framework import serializers
from .models import Attendance, LeaveBalance, RecentActivities, LeaveRequest
from rest_framework.exceptions import ValidationError

class AttendanceSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"field1": "value1", "field2": "value2"}
        self.invalid_data = {"field1": "", "field2": "value2"}

    def test_valid_attendance_serializer(self):
        serializer = AttendanceSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_attendance_serializer(self):
        serializer = AttendanceSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('field1', serializer.errors)

class LeaveBalanceSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"leave_type": "sick", "balance": 10}
        self.invalid_data = {"leave_type": "", "balance": -5}

    def test_valid_leave_balance_serializer(self):
        serializer = LeaveBalanceSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_leave_balance_serializer(self):
        serializer = LeaveBalanceSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('leave_type', serializer.errors)
        self.assertIn('balance', serializer.errors)

class RecentActivitiesSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"activity": "login", "timestamp": "2023-10-01T12:00:00Z"}
        self.invalid_data = {"activity": "", "timestamp": "invalid-date"}

    def test_valid_recent_activities_serializer(self):
        serializer = RecentActivitiesSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_recent_activities_serializer(self):
        serializer = RecentActivitiesSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('activity', serializer.errors)
        self.assertIn('timestamp', serializer.errors)

class LeaveRequestSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"leave_type": "casual", "start_date": "2023-10-15", "end_date": "2023-10-18", "reason": "Family event"}
        self.invalid_data = {"leave_type": "", "start_date": "invalid-date", "end_date": "", "reason": "Too short"}

    def test_valid_leave_request_serializer(self):
        serializer = LeaveRequestSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_leave_request_serializer(self):
        serializer = LeaveRequestSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('leave_type', serializer.errors)
        self.assertIn('start_date', serializer.errors)
        self.assertIn('end_date', serializer.errors)
        self.assertIn('reason', serializer.errors)

class AttendanceDetailSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"date": "2023-10-01", "status": "Present"}
        self.invalid_data = {"date": "invalid-date", "status": ""}

    def test_valid_attendance_detail_serializer(self):
        serializer = AttendanceDetailSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_attendance_detail_serializer(self):
        serializer = AttendanceDetailSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)
        self.assertIn('status', serializer.errors)

    def test_edge_case_empty_input(self):
        serializer = AttendanceDetailSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)
        self.assertIn('status', serializer.errors)

    def test_edge_case_invalid_types(self):
        serializer = AttendanceDetailSerializer(data={"date": 12345, "status": None})
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)
        self.assertIn('status', serializer.errors)

class EmployeeSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}
        self.invalid_data = {"first_name": "", "last_name": "", "email": "invalid-email"}

    def test_valid_employee_serializer(self):
        serializer = EmployeeSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_employee_serializer(self):
        serializer = EmployeeSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('first_name', serializer.errors)
        self.assertIn('last_name', serializer.errors)
        self.assertIn('email', serializer.errors)

class EmployeeProfileSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"employee_id": 1, "name": "Jane Doe", "email": "jane.doe@example.com", "phone": "1234567890", "address": "123 Main St"}
        self.invalid_data = {"employee_id": "invalid", "name": "", "email": "invalid-email", "phone": "invalid-phone", "address": ""}

    def test_valid_employee_profile_serializer(self):
        serializer = EmployeeProfileSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_employee_profile_serializer(self):
        serializer = EmployeeProfileSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('employee_id', serializer.errors)
        self.assertIn('name', serializer.errors)
        self.assertIn('email', serializer.errors)
        self.assertIn('phone', serializer.errors)
        self.assertIn('address', serializer.errors)

class AttendanceReportResponseSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"attendance_report": [{"employee_id": 1, "date": "2023-10-01", "status": "Present"}], "manager_id": 1, "start_date": "2023-10-01", "end_date": "2023-10-31"}
        self.invalid_data = {"attendance_report": [], "manager_id": -1, "start_date": "invalid-date", "end_date": ""}

    def test_valid_attendance_report_response_serializer(self):
        serializer = AttendanceReportResponseSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_attendance_report_response_serializer(self):
        serializer = AttendanceReportResponseSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('manager_id', serializer.errors)
        self.assertIn('start_date', serializer.errors)
        self.assertIn('end_date', serializer.errors)

class NotificationSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"employee": 1, "message": "Test notification", "is_read": False, "timestamp": "2023-10-01T12:00:00Z"}
        self.invalid_data = {"employee": "invalid", "message": "", "is_read": "wrong_type"}

    def test_valid_notification_serializer(self):
        serializer = NotificationSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_notification_serializer(self):
        serializer = NotificationSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('employee', serializer.errors)
        self.assertIn('message', serializer.errors)
        self.assertIn('is_read', serializer.errors)

class RoleSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"name": "Admin", "permissions": ["view", "edit"]}
        self.invalid_data = {"name": "", "permissions": "invalid_permissions"}

    def test_valid_role_serializer(self):
        serializer = RoleSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_role_serializer(self):
        serializer = RoleSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
        self.assertIn('permissions', serializer.errors)

class RoleCreateSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"name": "User", "permissions": ["view"]}
        self.invalid_data = {"name": "", "permissions": "wrong_permissions"}

    def test_valid_role_create_serializer(self):
        serializer = RoleCreateSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_role_create_serializer(self):
        serializer = RoleCreateSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
        self.assertIn('permissions', serializer.errors)

class RoleUpdateSerializerTestCase(serializers.ModelSerializer):
    def setUp(self):
        self.valid_data = {"permissions": ["edit"]}
        self.invalid_data = {"permissions": "invalid_permissions"}

    def test_valid_role_update_serializer(self):
        serializer = RoleUpdateSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.valid_data)

    def test_invalid_role_update_serializer(self):
        serializer = RoleUpdateSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('permissions', serializer.errors)