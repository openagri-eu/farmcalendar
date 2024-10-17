from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class FarmActivitiesTests(TestCase):

    def setUp(self):
        # Create a user to be logged in, as the views require login
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_calendar_activity_list_returns_200(self):
        # Log in the test client as the user (since the view requires login)
        self.client.login(username='testuser', password='testpass')

        # Get the URL for the 'calendar_activity_list' view
        url = reverse('calendar_activity_list')

        # Send a GET request to the view
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
