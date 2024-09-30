from django.shortcuts import render
from django.http import JsonResponse
from .models import Attendance, Leave, Activity

# Create your views here.

def get_attendance(request, employee_id):
    attendance_data = Attendance.objects.filter(employee_id=employee_id).values()  # Modify accordingly to your needs
    return JsonResponse(list(attendance_data), safe=False)

def get_leave_balance(request, employee_id):
    leave_balance = Leave.objects.filter(employee_id=employee_id).values('balance')  # Modify accordingly to your needs
    return JsonResponse(list(leave_balance), safe=False)

def get_recent_activities(request, employee_id):
    activities = Activity.objects.filter(employee_id=employee_id).values()  # Modify accordingly to your needs
    return JsonResponse(list(activities), safe=False)