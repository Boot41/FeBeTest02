from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch
from .models import Attendance
from .services import generate_attendance_report

class AttendanceReportTests(TestCase):
    @patch('yourapp.models.Attendance.objects.filter')
    def test_generate_attendance_report_success(self, mock_filter):
        # Arrange
        manager_id = 1
        start_date = timezone.now().date()
        end_date = start_date
        mock_filter.return_value.values.return_value.annotate.return_value.order_by.return_value = [
            {'employee__name': 'John Doe', 'total_days': 5, 'present_days': 3},
            {'employee__name': 'Jane Doe', 'total_days': 4, 'present_days': 4}
        ]

        # Act
        report = generate_attendance_report(manager_id, start_date, end_date)

        # Assert
        self.assertEqual(len(report), 2)
        self.assertEqual(report[0]['employee__name'], 'John Doe')
        self.assertEqual(report[0]['total_days'], 5)
        self.assertEqual(report[0]['present_days'], 3)

    @patch('yourapp.models.Attendance.objects.filter')
    def test_generate_attendance_report_no_results(self, mock_filter):
        # Arrange
        manager_id = 1
        start_date = timezone.now().date()
        end_date = start_date
        mock_filter.return_value.values.return_value.annotate.return_value.order_by.return_value = []

        # Act
        report = generate_attendance_report(manager_id, start_date, end_date)

        # Assert
        self.assertEqual(report, [])

    @patch('yourapp.models.Attendance.objects.filter')
    def test_generate_attendance_report_invalid_manager_id(self, mock_filter):
        # Arrange
        manager_id = None
        start_date = timezone.now().date()
        end_date = start_date
        mock_filter.return_value.values.return_value.annotate.return_value.order_by.return_value = []

        # Act and Assert
        with self.assertRaises(TypeError):
            generate_attendance_report(manager_id, start_date, end_date)

    @patch('yourapp.models.Attendance.objects.filter')
    def test_generate_attendance_report_invalid_dates(self, mock_filter):
        # Arrange
        manager_id = 1
        start_date = 'invalid_date'
        end_date = 'invalid_date'

        # Act and Assert
        with self.assertRaises(ValueError):
            generate_attendance_report(manager_id, start_date, end_date)

    @patch('yourapp.models.Attendance.objects.filter')
    def test_generate_attendance_report_edge_case_empty_dates(self, mock_filter):
        # Arrange
        manager_id = 1
        start_date = None
        end_date = None
        mock_filter.return_value.values.return_value.annotate.return_value.order_by.return_value = []

        # Act
        report = generate_attendance_report(manager_id, start_date, end_date)

        # Assert
        self.assertEqual(report, [])