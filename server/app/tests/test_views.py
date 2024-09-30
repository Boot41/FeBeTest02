import unittest
from unittest.mock import patch, MagicMock
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class MyApiTests(APITestCase):

    def setUp(self):
        self.valid_payload = {"name": "Test", "email": "test@example.com"}
        self.invalid_payload = {"name": "", "email": ""}

    @patch('app.models.MyModel.objects.create')
    def test_create_valid_data(self, mock_create):
        mock_create.return_value = MagicMock(id=1)
        response = self.client.post(reverse('my_endpoint'), self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], 1)

    def test_create_invalid_data(self):
        response = self.client.post(reverse('my_endpoint'), self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('app.models.MyModel.objects.get')
    def test_get_valid_entry(self, mock_get):
        mock_get.return_value = MagicMock(**self.valid_payload)
        response = self.client.get(reverse('my_endpoint', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.valid_payload['name'])

    @patch('app.models.MyModel.objects.get')
    def test_get_invalid_entry(self, mock_get):
        mock_get.side_effect = Exception("Not Found")
        response = self.client.get(reverse('my_endpoint', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @patch('app.models.MyModel.objects.update')
    def test_update_valid_data(self, mock_update):
        mock_update.return_value = None
        response = self.client.put(reverse('my_endpoint', args=[1]), self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_data(self):
        response = self.client.put(reverse('my_endpoint', args=[1]), self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('app.models.MyModel.objects.delete')
    def test_delete_valid_entry(self, mock_delete):
        mock_delete.return_value = None
        response = self.client.delete(reverse('my_endpoint', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @patch('app.models.MyModel.objects.delete')
    def test_delete_invalid_entry(self, mock_delete):
        mock_delete.side_effect = Exception("Not Found")
        response = self.client.delete(reverse('my_endpoint', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @patch('app.models.Attendance.objects.filter')
    def test_get_attendance_valid(self, mock_filter):
        mock_filter.return_value.values.return_value = [{"date": "2023-01-01", "status": "Present"}]
        response = self.client.get(reverse('get_attendance', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @patch('app.models.Attendance.objects.filter')
    def test_get_attendance_no_records(self, mock_filter):
        mock_filter.return_value.values.return_value = []
        response = self.client.get(reverse('get_attendance', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    @patch('app.models.LeaveBalance.objects.filter')
    def test_get_leave_balance_valid(self, mock_filter):
        mock_filter.return_value.values.return_value = [{"leave_type": "Sick", "balance": 5}]
        response = self.client.get(reverse('get_leave_balance', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @patch('app.models.RecentActivity.objects.filter')
    def test_get_recent_activities_valid(self, mock_filter):
        mock_filter.return_value.values.return_value = [{"activity": "Logged in"}]
        response = self.client.get(reverse('get_recent_activities', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_request_leave_valid(self):
        response = self.client.post(reverse('request_leave', args=[1]), {"leave_type": "Sick", "days": 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], 'Leave request submitted.')

    def test_request_leave_invalid_method(self):
        response = self.client.get(reverse('request_leave', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('app.models.LeaveBalance.objects.filter')
    def test_get_team_attendance_valid(self, mock_filter):
        mock_filter.return_value.values.return_value = [{"employee_id": 1, "date": "2023-01-01", "status": "Present"}]
        response = self.client.get(reverse('get_team_attendance', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @patch('app.models.LeaveBalance.objects.filter')
    def test_get_team_leave_requests_valid(self, mock_filter):
        mock_filter.return_value.values.return_value = [{"employee_id": 1, "leave_type": "Sick", "balance": 5}]
        response = self.client.get(reverse('get_team_leave_requests', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_approve_leave_request_valid(self):
        response = self.client.post(reverse('approve_leave_request', args=[1, 1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], 'Leave request approved.')

    def test_approve_leave_request_invalid_method(self):
        response = self.client.get(reverse('approve_leave_request', args=[1, 1]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_deny_leave_request_valid(self):
        response = self.client.post(reverse('deny_leave_request', args=[1, 1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], 'Leave request denied.')

    def test_deny_leave_request_invalid_method(self):
        response = self.client.get(reverse('deny_leave_request', args=[1, 1]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('app.models.Employee.objects.values')
    def test_get_organization_directory(self, mock_values):
        mock_values.return_value = [{"employee_id": 1, "name": "John Doe"}]
        response = self.client.get(reverse('get_organization_directory'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @patch('app.models.Employee.objects.values')
    def test_get_organization_structure(self, mock_values):
        response = self.client.get(reverse('get_organization_structure'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    @patch('app.models.Employee.objects.get')
    def test_get_employee_profile_valid(self, mock_get):
        mock_get.return_value = MagicMock(employee_id=1, name='John Doe')
        response = self.client.get(reverse('get_employee_profile', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')

    @patch('app.models.Employee.objects.get')
    def test_get_employee_profile_not_found(self, mock_get):
        mock_get.side_effect = Employee.DoesNotExist
        response = self.client.get(reverse('get_employee_profile', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_employee_profile_invalid_method(self):
        response = self.client.post(reverse('get_employee_profile', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('app.models.Employee.objects.get')
    def test_update_employee_profile_valid(self, mock_get):
        mock_get.return_value = MagicMock(employee_id=1, name='John Doe')
        response = self.client.put(reverse('update_employee_profile', args=[1]), {"name": "Jane Doe"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('app.models.Employee.objects.get')
    def test_update_employee_profile_not_found(self, mock_get):
        mock_get.side_effect = Employee.DoesNotExist
        response = self.client.put(reverse('update_employee_profile', args=[999]), {"name": "Jane Doe"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee_profile_invalid_method(self):
        response = self.client.post(reverse('update_employee_profile', args=[1]), {"name": "Jane Doe"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_employee_profile_invalid_json(self):
        response = self.client.put(reverse('update_employee_profile', args=[1]), "Invalid JSON")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)