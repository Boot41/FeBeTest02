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