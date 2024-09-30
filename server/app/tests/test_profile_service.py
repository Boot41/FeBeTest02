from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee

class EmployeeProfileTests(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(employee_id=1, name='John Doe', position='Developer')

    def test_get_employee_profile_success(self):
        response = self.client.get(reverse('get_employee_profile', args=[self.employee.employee_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.employee.name)

    def test_get_employee_profile_not_found(self):
        response = self.client.get(reverse('get_employee_profile', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Employee not found.')

    def test_update_employee_profile_success(self):
        response = self.client.put(reverse('update_employee_profile', args=[self.employee.employee_id]),
                                   {'name': 'Jane Doe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.name, 'Jane Doe')

    def test_update_employee_profile_not_found(self):
        response = self.client.put(reverse('update_employee_profile', args=[999]), {'name': 'Unknown'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Employee not found.')

    def test_update_employee_profile_invalid_data(self):
        response = self.client.put(reverse('update_employee_profile', args=[self.employee.employee_id]),
                                   {'name': ''})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
