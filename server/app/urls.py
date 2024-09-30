from django.urls import path
from .views import get_attendance, get_leave_balance, get_recent_activities, request_leave

urlpatterns = [
    path('employee/<int:employee_id>/attendance-details', get_attendance, name='fetch_attendance'),
    path('employee/<int:employee_id>/leave-balance', get_leave_balance, name='fetch_leave_balance'),
    path('employee/<int:employee_id>/recent-activities', get_recent_activities, name='fetch_recent_activities'),
    path('employee/<int:employee_id>/request-leave', request_leave, name='request_leave'),
    path('manager/<int:manager_id>/team-attendance', get_team_attendance, name='fetch_team_attendance'),
    path('manager/<int:manager_id>/team-leave-requests', get_team_leave_requests, name='fetch_team_leave_requests'),
    path('manager/<int:manager_id>/leave-requests/<int:request_id>/approve', approve_leave_request, name='approve_leave_request'),
    path('manager/<int:manager_id>/leave-requests/<int:request_id>/deny', deny_leave_request, name='deny_leave_request'),
]