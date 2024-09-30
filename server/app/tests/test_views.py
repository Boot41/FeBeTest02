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
