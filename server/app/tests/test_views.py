from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from .models import Attendance, Leave, Activity

class AttendanceViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.employee_id = 1
        Attendance.objects.create(employee_id=self.employee_id, date='2023-01-01', status='Present')
        Leave.objects.create(employee_id=self.employee_id, balance=10)
        Activity.objects.create(employee_id=self.employee_id, activity='Check-in')

    def test_get_attendance_success(self):
        response = self.client.get(reverse('get_attendance', args=[self.employee_id]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_attendance_not_found(self):
        response = self.client.get(reverse('get_attendance', args=[999]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    @patch('app.models.Attendance.objects.filter')
    def test_get_attendance_database_error(self, mock_filter):
        mock_filter.side_effect = Exception('Database error')
        with self.assertRaises(Exception):
            self.client.get(reverse('get_attendance', args=[self.employee_id]))

    def test_get_leave_balance_success(self):
        response = self.client.get(reverse('get_leave_balance', args=[self.employee_id]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)

    def test_get_leave_balance_not_found(self):
        response = self.client.get(reverse('get_leave_balance', args=[999]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    @patch('app.models.Leave.objects.filter')
    def test_get_leave_balance_database_error(self, mock_filter):
        mock_filter.side_effect = Exception('Database error')
        with self.assertRaises(Exception):
            self.client.get(reverse('get_leave_balance', args=[self.employee_id]))

    def test_get_recent_activities_success(self):
        response = self.client.get(reverse('get_recent_activities', args=[self.employee_id]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_recent_activities_not_found(self):
        response = self.client.get(reverse('get_recent_activities', args=[999]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    @patch('app.models.Activity.objects.filter')
    def test_get_recent_activities_database_error(self, mock_filter):
        mock_filter.side_effect = Exception('Database error')
        with self.assertRaises(Exception):
            self.client.get(reverse('get_recent_activities', args=[self.employee_id]))