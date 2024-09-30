from django.test import TestCase
from unittest.mock import patch, MagicMock
from rest_framework import status
from .models import LeaveBalance
from .views import request_leave

class LeaveServiceTestCase(TestCase):
    @patch('app.views.get_object_or_404')
    def test_request_leave_success(self, mock_get_object_or_404):
        leave_balance_mock = MagicMock()
        leave_balance_mock.balance = 10
        mock_get_object_or_404.return_value = leave_balance_mock

        response = request_leave(employee_id=1, leave_type='vacation', days=5)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Leave requested successfully.'})
        leave_balance_mock.save.assert_called_once()
        self.assertEqual(leave_balance_mock.balance, 5)

    @patch('app.views.get_object_or_404')
    def test_request_leave_insufficient_balance(self, mock_get_object_or_404):
        leave_balance_mock = MagicMock()
        leave_balance_mock.balance = 2
        mock_get_object_or_404.return_value = leave_balance_mock

        response = request_leave(employee_id=1, leave_type='vacation', days=5)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Insufficient leave balance.'})
        leave_balance_mock.save.assert_not_called()

    @patch('app.views.get_object_or_404')
    def test_request_leave_not_found(self, mock_get_object_or_404):
        mock_get_object_or_404.side_effect = Http404

        response = request_leave(employee_id=1, leave_type='vacation', days=5)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @patch('app.views.get_object_or_404')
    def test_request_leave_invalid_days(self, mock_get_object_or_404):
        leave_balance_mock = MagicMock()
        leave_balance_mock.balance = 10
        mock_get_object_or_404.return_value = leave_balance_mock

        response = request_leave(employee_id=1, leave_type='vacation', days='invalid')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    @patch('app.views.get_object_or_404')
    def test_request_leave_zero_days(self, mock_get_object_or_404):
        leave_balance_mock = MagicMock()
        leave_balance_mock.balance = 10
        mock_get_object_or_404.return_value = leave_balance_mock

        response = request_leave(employee_id=1, leave_type='vacation', days=0)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Insufficient leave balance.'})