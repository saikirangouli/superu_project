from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import user_profile

class UserProfileTests(APITestCase):
    def setUp(self):
        self.user = user_profile.objects.create(name='test_user', email='testemail@example.com', bio='test bio')

    def test_create_profile(self):
        url = reverse('user-profile')
        access_token_url = reverse('token_obtain_pair')
        data = {'username':'kiran','password':'1234'}
        access_token = self.client.post(access_token_url,data,format='json')
        print(access_token)
        data = {'name': 'Alice Smith', 'email': 'alice@example.com', 'bio': 'Test bio'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user_profile.objects.count(), 2)

    def test_update_profile(self):
        url = reverse('user-profile', args=[self.user.id])
        data = {'name': 'new test name'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, 'new test name')


