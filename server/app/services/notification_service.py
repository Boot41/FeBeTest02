from django.db import models

class Notification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.employee.name}: {self.message}"

    @classmethod
    def create_notification(cls, employee, message):
        notification = cls(employee=employee, message=message)
        notification.save()
        return notification

    @classmethod
    def get_notifications(cls, employee_id):
        return cls.objects.filter(employee_id=employee_id).order_by('-created_at')

    @classmethod
    def mark_as_read(cls, notification_id):
        try:
            notification = cls.objects.get(id=notification_id)
            notification.is_read = True
            notification.save()
            return notification
        except cls.DoesNotExist:
            return None



from django.http import JsonResponse
from .models import Notification


def fetch_notifications(request, employee_id):
    if request.method == 'GET':
        notifications = Notification.get_notifications(employee_id)
        return JsonResponse(list(notifications.values()), safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def mark_notification_as_read(request, employee_id, notification_id):
    if request.method == 'POST':
        notification = Notification.mark_as_read(notification_id)
        if notification:
            return JsonResponse({'message': 'Notification marked as read.'}, status=200)
        return JsonResponse({'error': 'Notification not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)