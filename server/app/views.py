from django.shortcuts import render
from django.http import JsonResponse
from .models import Attendance, LeaveBalance, RecentActivity, Employee

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


def get_team_attendance(request, manager_id):
    team_attendance = Attendance.objects.filter(employee__manager_id=manager_id).values('employee_id', 'date', 'status')
    return JsonResponse(list(team_attendance), safe=False)


def get_team_leave_requests(request, manager_id):
    leave_requests = LeaveBalance.objects.filter(employee__manager_id=manager_id).values('employee_id', 'leave_type', 'balance')  # Modify accordingly to your needs
    return JsonResponse(list(leave_requests), safe=False)


def approve_leave_request(request, manager_id, request_id):
    if request.method == 'POST':
        # Logic to approve leave request goes here, e.g., updating the database
        return JsonResponse({'message': 'Leave request approved.'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def deny_leave_request(request, manager_id, request_id):
    if request.method == 'POST':
        # Logic to deny leave request goes here, e.g., updating the database
        return JsonResponse({'message': 'Leave request denied.'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def get_organization_directory(request):
    employees = Employee.objects.all().values('employee_id', 'name')  # Add additional fields as needed
    return JsonResponse(list(employees), safe=False)


def get_organization_structure(request):
    # Logic to fetch organization structure, e.g., using Employee model's manager relationship
    # An example placeholder for hierarchical data
    return JsonResponse({'structure': 'Sample structure data'}, safe=False)