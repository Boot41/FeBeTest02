from django.db import models

# Create your models here.

from rest_framework import serializers
from .models import Attendance, LeaveBalance, RecentActivities

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class LeaveBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveBalance
        fields = '__all__'

class RecentActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentActivities
        fields = '__all__'
