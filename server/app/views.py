from django.shortcuts import render
from django.http import JsonResponse
from .models import Attendance, LeaveBalance, RecentActivity, Employee, LeaveRequest, Notification, Role
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.dateparse import parse_date
from datetime import timedelta

# Create your views here.

def get_notifications(request, employee_id):
    notifications = Notification.objects.filter(employee_id=employee_id).values('id', 'message', 'status')
    return JsonResponse(list(notifications), safe=False)

@csrf_exempt
def mark_notification_as_read(request, employee_id, notification_id):
    if request.method == 'POST':
        try:
            notification = Notification.objects.get(id=notification_id, employee_id=employee_id)
            notification.status = 'read'
            notification.save()
            return JsonResponse({'message': 'Notification marked as read.'}, status=200)
        except Notification.DoesNotExist:
            return JsonResponse({'error': 'Notification not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def fetch_roles(request):
    if request.method == 'GET':
        roles = Role.objects.all().values('id', 'name', 'permissions')
        return JsonResponse(list(roles), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def create_role(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            role = Role.objects.create(name=data['name'], permissions=data['permissions'])
            return JsonResponse({'id': role.id, 'name': role.name, 'permissions': role.permissions}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def update_role(request, role_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            role = Role.objects.get(id=role_id)
            role.permissions = data['permissions']
            role.save()
            return JsonResponse({'message': 'Role updated successfully.'}, status=200)
        except Role.DoesNotExist:
            return JsonResponse({'error': 'Role not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def delete_role(request, role_id):
    if request.method == 'DELETE':
        try:
            role = Role.objects.get(id=role_id)
            role.delete()
            return JsonResponse({'message': 'Role deleted successfully.'}, status=200)
        except Role.DoesNotExist:
            return JsonResponse({'error': 'Role not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def link_calendar(request, employee_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Simulate linking the calendar here
        # For real integration, you would use an API to link the calendar
        return JsonResponse({'message': 'Calendar linked successfully for employee ID: {}'.format(employee_id)}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def fetch_calendar_events(request, employee_id):
    if request.method == 'GET':
        # Simulate fetching calendar events for attendance logging
        events = [
            {'event_id': 1, 'title': 'Meeting', 'start': '2023-10-15T10:00:00Z', 'end': '2023-10-15T11:00:00Z'},
            {'event_id': 2, 'title': 'Work Session', 'start': '2023-10-15T11:30:00Z', 'end': '2023-10-15T12:30:00Z'}
        ]
        return JsonResponse({'events': events}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

... (existing view functions)