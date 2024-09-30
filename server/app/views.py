from django.shortcuts import render
from django.http import JsonResponse
from .models import Attendance, LeaveBalance, RecentActivity, Employee, LeaveRequest, Notification
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

... (existing view functions)