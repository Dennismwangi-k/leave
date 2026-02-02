from django.test import TestCase, Client
from django.urls import reverse
from .models import LeaveRequest
from datetime import date

class LeaveRequestModelTest(TestCase):
    def test_leave_days_calculation_excludes_weekends(self):
        leave_request = LeaveRequest(
            person="Test Person",
            start_date=date(2023, 10, 27),
            end_date=date(2023, 10, 30),
            leave_type='normal'
        )
        self.assertEqual(leave_request.leave_days, 2)

    def test_leave_days_calculation_weekdays_only(self):
        leave_request = LeaveRequest(
            person="Test Person",
            start_date=date(2023, 10, 23),
            end_date=date(2023, 10, 25),
            leave_type='normal'
        )
        self.assertEqual(leave_request.leave_days, 3)

    def test_leave_days_zero_if_dates_missing(self):
        leave_request = LeaveRequest(person="Test Person")
        self.assertEqual(leave_request.leave_days, 0)


class LeaveRequestViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.leave_request = LeaveRequest.objects.create(
            person="Existing Person",
            start_date=date(2023, 11, 1),
            end_date=date(2023, 11, 2),
            leave_type='normal'
        )

    def test_list_view_status_code(self):
        try:
            url = reverse('leave_list')
        except:
            return 
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_request_via_list_view(self):
        url = reverse('leave_list')
        data = {
            'person': 'New Person',
            'start_date': '2023-12-01',
            'end_date': '2023-12-05',
            'leave_type': 'sick'
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, url)
        self.assertTrue(LeaveRequest.objects.filter(person='New Person').exists())

    def test_create_request_invalid_shows_modal(self):
        url = reverse('leave_list')
        data = {
            'person': 'Incomplete Person',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('show_modal', response.context)
        self.assertTrue(response.context['show_modal'])
        self.assertFalse(LeaveRequest.objects.filter(person='Incomplete Person').exists())

