from django.shortcuts import render
from django.http import JsonResponse
from .models import Attendance, LeaveBalance, RecentActivity

# Create your views here.

def get_attendance(request, employee_id):
    attendance_data = Attendance.objects.filter(employee_id=employee_id).values()  # Modify accordingly to your needs
    return JsonResponse(list(attendance_data), safe=False)

def get_leave_balance(request, employee_id):
    leave_balance = LeaveBalance.objects.filter(employee_id=employee_id).values('leave_type', 'balance')  # Modify accordingly to your needs
    return JsonResponse(list(leave_balance), safe=False)

def get_recent_activities(request, employee_id):
    activities = RecentActivity.objects.filter(employee_id=employee_id).values()  # Modify accordingly to your needs
    return JsonResponse(list(activities), safe=False)

def request_leave(request, employee_id):
    if request.method == 'POST':
        # Logic for leave request goes here, e.g., saving to database
        return JsonResponse({'message': 'Leave request submitted.'}, status=201)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)