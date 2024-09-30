from django.db.models import Count
from .models import Attendance

# Calculate attendance reports for a manager's team within a specified date range.

def generate_attendance_report(manager_id, start_date, end_date):
    report = Attendance.objects.filter(employee__manager_id=manager_id, date__range=(start_date, end_date))
    report_summary = report.values('employee__name').annotate(total_days=Count('date'), present_days=Count('date', filter=(Q(status='present')))).order_by('employee__name')
    return list(report_summary)

# Existing code can go here as needed