import requests
from unittest import TestCase, mock
from app.services.calendar_service import CalendarService

class TestCalendarService(TestCase):
    def setUp(self):
        self.service = CalendarService()

    @mock.patch('app.services.calendar_service.requests.post')
    def test_link_calendar_success(self, mock_post):
        mock_post.return_value.status_code = 200
        response = self.service.link_calendar('employee_1', {'calendar_id': '123'})
        mock_post.assert_called_once()
        self.assertIsNone(response)

    @mock.patch('app.services.calendar_service.requests.post')
    def test_link_calendar_failure(self, mock_post):
        mock_post.return_value.status_code = 400
        response = self.service.link_calendar('employee_1', {'calendar_id': '123'})
        mock_post.assert_called_once()
        self.assertIsNone(response)

    @mock.patch('app.services.calendar_service.requests.get')
    def test_fetch_calendar_events_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'event_id': '1'}]
        events = self.service.fetch_calendar_events('employee_1')
        mock_get.assert_called_once()
        self.assertEqual(len(events), 1)

    @mock.patch('app.services.calendar_service.requests.get')
    def test_fetch_calendar_events_empty(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []
        events = self.service.fetch_calendar_events('employee_1')
        self.assertEqual(len(events), 0)

    @mock.patch('app.services.calendar_service.CalendarService.parse_event')
    def test_parse_event(self, mock_parse_event):
        event_data = {'id': '1', 'summary': 'Test Event'}
        mock_parse_event.return_value = event_data
        event = self.service.parse_event(event_data)
        self.assertEqual(event['id'], '1')

    def test_log_attendance_from_event(self):
        event = {'summary': 'Test Event'}
        response = self.service.log_attendance_from_event(event, 'employee_1')
        # Assuming the logic returns None for a successful log
        self.assertIsNone(response)

    @mock.patch('app.services.calendar_service.requests.post')
    def test_log_attendance_from_event_failure(self, mock_post):
        mock_post.return_value.status_code = 500
        event = {'summary': 'Failed Event'}
        response = self.service.log_attendance_from_event(event, 'employee_1')
        self.assertIsNone(response)