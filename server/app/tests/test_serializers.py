from rest_framework import serializers
from .models import Attendance, LeaveBalance, RecentActivities
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