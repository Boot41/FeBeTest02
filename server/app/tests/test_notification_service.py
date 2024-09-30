from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch, MagicMock
from .models import Notification, Employee

class NotificationTests(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='John Doe')
        self.notification = Notification.create_notification(self.employee, 'Test message')

    def test_create_notification(self):
        notification = Notification.create_notification(self.employee, 'New notification')
        self.assertEqual(notification.message, 'New notification')
        self.assertFalse(notification.is_read)

    def test_get_notifications(self):
        notifications = Notification.get_notifications(self.employee.id)
        self.assertEqual(len(notifications), 1)
        self.assertEqual(notifications[0].message, 'Test message')

    def test_mark_as_read_success(self):
        response = Notification.mark_as_read(self.notification.id)
        self.assertIsNotNone(response)
        self.assertTrue(response.is_read)

    def test_mark_as_read_not_found(self):
        response = Notification.mark_as_read(999)
        self.assertIsNone(response)

    @patch('app.views.Notification.get_notifications')
    def test_fetch_notifications_success(self, mock_get_notifications):
        mock_get_notifications.return_value = [self.notification]
        response = self.client.get(reverse('fetch_notifications', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_fetch_notifications_invalid_method(self):
        response = self.client.post(reverse('fetch_notifications', args=[self.employee.id]))
        self.assertEqual(response.status_code, 400)

    @patch('app.views.Notification.mark_as_read')
    def test_mark_notification_as_read_success(self, mock_mark_as_read):
        mock_mark_as_read.return_value = self.notification
        response = self.client.post(reverse('mark_notification_as_read', args=[self.employee.id, self.notification.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Notification marked as read.', response.json().get('message'))

    @patch('app.views.Notification.mark_as_read')
    def test_mark_notification_as_read_not_found(self, mock_mark_as_read):
        mock_mark_as_read.return_value = None
        response = self.client.post(reverse('mark_notification_as_read', args=[self.employee.id, 999]))
        self.assertEqual(response.status_code, 404)
        self.assertIn('Notification not found.', response.json().get('error'))

    def test_mark_notification_as_read_invalid_method(self):
        response = self.client.get(reverse('mark_notification_as_read', args=[self.employee.id, self.notification.id]))
        self.assertEqual(response.status_code, 400)