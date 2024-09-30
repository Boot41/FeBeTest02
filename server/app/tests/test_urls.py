from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch

class AttendanceAPITests(APITestCase):
    def test_get_attendance_success(self):
        url = reverse('employee-attendance', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_attendance_not_found(self):
        url = reverse('employee-attendance', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_attendance_invalid_employee_id(self):
        url = reverse('employee-attendance', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LeaveBalanceAPITests(APITestCase):
    def test_get_leave_balance_success(self):
        url = reverse('employee-leave-balance', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_leave_balance_not_found(self):
        url = reverse('employee-leave-balance', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_leave_balance_invalid_employee_id(self):
        url = reverse('employee-leave-balance', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RecentActivitiesAPITests(APITestCase):
    def test_get_recent_activities_success(self):
        url = reverse('employee-recent-activities', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_recent_activities_not_found(self):
        url = reverse('employee-recent-activities', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_recent_activities_invalid_employee_id(self):
        url = reverse('employee-recent-activities', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)