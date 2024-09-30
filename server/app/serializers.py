from django.db import models

from rest_framework import serializers
from .models import Attendance, LeaveBalance, RecentActivity
from .models import LeaveRequest, Employee, Notification
from .models import Role

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class LeaveBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveBalance
        fields = '__all__'

class RecentActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentActivity
        fields = '__all__'

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'email', 'phone', 'address']

class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['employee_id', 'date', 'status']

class AttendanceReportResponseSerializer(serializers.Serializer):
    attendance_report = AttendanceReportSerializer(many=True)
    manager_id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'employee', 'message', 'is_read', 'timestamp']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions']

class RoleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name', 'permissions']

class RoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['permissions']