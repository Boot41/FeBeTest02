from django.urls import path
from .views import get_attendance, get_leave_balance, get_recent_activities, request_leave

urlpatterns = [
    path('employee/<int:employee_id>/attendance-details', get_attendance, name='fetch_attendance'),
    path('employee/<int:employee_id>/leave-balance', get_leave_balance, name='fetch_leave_balance'),
    path('employee/<int:employee_id>/recent-activities', get_recent_activities, name='fetch_recent_activities'),
    path('employee/<int:employee_id>/request-leave', request_leave, name='request_leave'),
]