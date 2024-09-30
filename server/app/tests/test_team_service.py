from django.test import TestCase
from unittest.mock import patch
from .models import Attendance, LeaveBalance
from .services import TeamService

class TeamServiceTest(TestCase):
    @patch('app.models.Attendance.objects.filter')
    def test_get_team_attendance(self, mock_filter):
        mock_filter.return_value = Attendance(
            id=1,
            manager_id=1,
            employee_id=1,
            status='present'
        )
        attendance = TeamService.get_team_attendance(1)
        self.assertEqual(attendance, mock_filter.return_value)
        mock_filter.assert_called_once_with(manager_id=1)

    @patch('app.models.LeaveBalance.objects.filter')
    def test_get_team_leave_requests(self, mock_filter):
        mock_filter.return_value = LeaveBalance(
            id=1,
            manager_id=1,
            request_id=1,
            status='pending'
        )
        leave_requests = TeamService.get_team_leave_requests(1)
        self.assertEqual(leave_requests, mock_filter.return_value)
        mock_filter.assert_called_once_with(manager_id=1)

    @patch('app.models.LeaveBalance.objects.get')
    def test_approve_leave_request(self, mock_get):
        mock_get.return_value.status = 'approved'
        TeamService.approve_leave_request(1, 1)
        mock_get.assert_called_once_with(id=1)
        self.assertEqual(mock_get.return_value.status, 'approved')

    @patch('app.models.LeaveBalance.objects.get')
    def test_deny_leave_request(self, mock_get):
        mock_get.return_value.status = 'denied'
        TeamService.deny_leave_request(1, 1)
        mock_get.assert_called_once_with(id=1)
        self.assertEqual(mock_get.return_value.status, 'denied')

    @patch('app.models.LeaveBalance.objects.get')
    def test_approve_leave_request_not_found(self, mock_get):
        mock_get.side_effect = Exception('Not Found')
        with self.assertRaises(Exception):
            TeamService.approve_leave_request(1, 999)

    @patch('app.models.LeaveBalance.objects.get')
    def test_deny_leave_request_not_found(self, mock_get):
        mock_get.side_effect = Exception('Not Found')
        with self.assertRaises(Exception):
            TeamService.deny_leave_request(1, 999)