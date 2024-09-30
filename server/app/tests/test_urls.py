from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch

class AttendanceAPITests(APITestCase):
    def test_get_attendance_success(self):
        url = reverse('fetch_attendance', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_attendance_not_found(self):
        url = reverse('fetch_attendance', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_attendance_invalid_employee_id(self):
        url = reverse('fetch_attendance', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LeaveBalanceAPITests(APITestCase):
    def test_get_leave_balance_success(self):
        url = reverse('fetch_leave_balance', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_leave_balance_not_found(self):
        url = reverse('fetch_leave_balance', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_leave_balance_invalid_employee_id(self):
        url = reverse('fetch_leave_balance', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class RecentActivitiesAPITests(APITestCase):
    def test_get_recent_activities_success(self):
        url = reverse('fetch_recent_activities', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_recent_activities_not_found(self):
        url = reverse('fetch_recent_activities', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_recent_activities_invalid_employee_id(self):
        url = reverse('fetch_recent_activities', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class AttendanceDetailsAPITests(APITestCase):
    def test_get_attendance_details_success(self):
        url = reverse('get_attendance', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_attendance_details_not_found(self):
        url = reverse('get_attendance', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_attendance_details_invalid_employee_id(self):
        url = reverse('get_attendance', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class RequestLeaveAPITests(APITestCase):
    def test_request_leave_success(self):
        url = reverse('request_leave', args=[1])
        response = self.client.post(url, data={'leave_type': 'sick', 'start_date': '2023-10-01', 'end_date': '2023-10-05'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_leave_not_found(self):
        url = reverse('request_leave', args=[999])
        response = self.client.post(url, data={'leave_type': 'sick', 'start_date': '2023-10-01', 'end_date': '2023-10-05'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_request_leave_invalid_employee_id(self):
        url = reverse('request_leave', args=['invalid'])
        response = self.client.post(url, data={'leave_type': 'sick'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TeamAttendanceAPITests(APITestCase):
    def test_get_team_attendance_success(self):
        url = reverse('fetch_team_attendance', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_team_attendance_not_found(self):
        url = reverse('fetch_team_attendance', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_team_attendance_invalid_manager_id(self):
        url = reverse('fetch_team_attendance', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TeamLeaveRequestsAPITests(APITestCase):
    def test_get_team_leave_requests_success(self):
        url = reverse('fetch_team_leave_requests', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_team_leave_requests_not_found(self):
        url = reverse('fetch_team_leave_requests', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_team_leave_requests_invalid_manager_id(self):
        url = reverse('fetch_team_leave_requests', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LeaveRequestApprovalAPITests(APITestCase):
    def test_approve_leave_request_success(self):
        url = reverse('approve_leave_request', args=[1, 1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_approve_leave_request_not_found(self):
        url = reverse('approve_leave_request', args=[1, 999])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_approve_leave_request_invalid_manager_id(self):
        url = reverse('approve_leave_request', args=['invalid', 1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LeaveRequestDenialAPITests(APITestCase):
    def test_deny_leave_request_success(self):
        url = reverse('deny_leave_request', args=[1, 1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deny_leave_request_not_found(self):
        url = reverse('deny_leave_request', args=[1, 999])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_deny_leave_request_invalid_manager_id(self):
        url = reverse('deny_leave_request', args=['invalid', 1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class OrganizationDirectoryAPITests(APITestCase):
    def test_get_organization_directory_success(self):
        url = reverse('get_organization_directory')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_organization_directory_failure(self):
        url = reverse('get_organization_directory')
        with patch('app.views.get_organization_directory') as mock:
            mock.side_effect = Exception('Database error')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

class OrganizationStructureAPITests(APITestCase):
    def test_get_organization_structure_success(self):
        url = reverse('get_organization_structure')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_organization_structure_failure(self):
        url = reverse('get_organization_structure')
        with patch('app.views.get_organization_structure') as mock:
            mock.side_effect = Exception('Database error')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_get_employee_profile_success(self):
        url = reverse('get_employee_profile', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_profile_not_found(self):
        url = reverse('get_employee_profile', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_employee_profile_invalid_employee_id(self):
        url = reverse('get_employee_profile', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_employee_profile_success(self):
        url = reverse('update_employee_profile', args=[1])
        response = self.client.put(url, data={'name': 'John Doe', 'position': 'Developer'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee_profile_not_found(self):
        url = reverse('update_employee_profile', args=[999])
        response = self.client.put(url, data={'name': 'John Doe'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee_profile_invalid_employee_id(self):
        url = reverse('update_employee_profile', args=['invalid'])
        response = self.client.put(url, data={'name': 'John Doe'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_employee_profile_missing_field(self):
        url = reverse('update_employee_profile', args=[1])
        response = self.client.put(url, data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_employee_profile_database_error(self):
        url = reverse('update_employee_profile', args=[1])
        with patch('app.views.update_employee_profile') as mock:
            mock.side_effect = Exception('Database error')
            response = self.client.put(url, data={'name': 'John Doe'})
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_get_employee_notifications_success(self):
        url = reverse('get_notifications', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_notifications_not_found(self):
        url = reverse('get_notifications', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_employee_notifications_invalid_employee_id(self):
        url = reverse('get_notifications', args=['invalid'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_mark_notification_as_read_success(self):
        url = reverse('mark_notification_as_read', args=[1, 1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_mark_notification_as_read_not_found(self):
        url = reverse('mark_notification_as_read', args=[1, 999])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_mark_notification_as_read_invalid_employee_id(self):
        url = reverse('mark_notification_as_read', args=['invalid', 1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)