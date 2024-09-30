from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

class LeaveBalance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    balance = models.IntegerField()

class RecentActivity(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, default='pending')
    reason = models.CharField(max_length=255)

class Organization(models.Model):
    name = models.CharField(max_length=255)

class EmployeeDirectory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class HierarchicalStructure(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='subordinates')
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='superiors')

class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)

class AttendanceReport(models.Model):
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_range_start = models.DateField()
    date_range_end = models.DateField()
    report_generated_on = models.DateTimeField(auto_now_add=True)
    attendance_data = models.JSONField()  # Store attendance data in JSON format

class Notification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
