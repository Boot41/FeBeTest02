from django.urls import path
from .views import get_attendance, get_leave_balance, get_recent_activities, request_leave
from .views import get_organization_directory, get_organization_structure
from .views import get_employee_profile, update_employee_profile
from .views import generate_attendance_report
from .views import get_notifications, mark_notification_as_read

urlpatterns = [
    path('employee/<int:employee_id>/attendance-details', get_attendance, name='fetch_attendance'),
    path('employee/<int:employee_id>/leave-balance', get_leave_balance, name='fetch_leave_balance'),
    path('employee/<int:employee_id>/recent-activities', get_recent_activities, name='fetch_recent_activities'),
    path('employee/<int:employee_id>/request-leave', request_leave, name='request_leave'),
    path('manager/<int:manager_id>/team-attendance', get_team_attendance, name='fetch_team_attendance'),
    path('manager/<int:manager_id>/team-leave-requests', get_team_leave_requests, name='fetch_team_leave_requests'),
    path('manager/<int:manager_id>/leave-requests/<int:request_id>/approve', approve_leave_request, name='approve_leave_request'),
    path('manager/<int:manager_id>/leave-requests/<int:request_id>/deny', deny_leave_request, name='deny_leave_request'),
    path('api/manager/<int:manager_id>/attendance-reports', generate_attendance_report, name='generate_attendance_report'),
    path('api/organization/directory', get_organization_directory, name='fetch_organization_directory'),
    path('api/organization/structure', get_organization_structure, name='fetch_organization_structure'),
    path('api/employee/<int:employee_id>/profile', get_employee_profile, name='get_employee_profile'),
    path('api/employee/<int:employee_id>/profile/update', update_employee_profile, name='update_employee_profile'),
    path('api/employee/<int:employee_id>/notifications', get_notifications, name='get_notifications'),
    path('api/employee/<int:employee_id>/notifications/<int:notification_id>/read', mark_notification_as_read, name='mark_notification_as_read'),
]