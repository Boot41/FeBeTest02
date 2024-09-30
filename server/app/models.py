from django.db import models

# Create your models here.

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