from django.urls import path
from .views import fetch_attendance, fetch_leave_balance, fetch_recent_activities

urlpatterns = [
    path('employee/<int:employee_id>/attendance', fetch_attendance, name='fetch_attendance'),
    path('employee/<int:employee_id>/leave-balance', fetch_leave_balance, name='fetch_leave_balance'),
    path('employee/<int:employee_id>/recent-activities', fetch_recent_activities, name='fetch_recent_activities'),
]
