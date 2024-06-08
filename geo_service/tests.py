from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from geo_service.models import QueryLog


class QueryViewSetTests(APITestCase):
    def test_create_query(self):
        """Проверка создания нового запроса"""
        url = reverse('query-list')
        data = {
            'cadastral_number': '12345678',
            'latitude': '50.0000',
            'longitude': '30.0000'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(QueryLog.objects.count(), 1)
        self.assertEqual(QueryLog.objects.get().cadastral_number, '12345678')

    def test_get_result(self):
        """Проверка получения результата"""
        test_data = {'cadastral_number': '12345678', 
                     'latitude': '50.0000', 
                     'longitude': '30.0000', 
                     'response': True}
        QueryLog.objects.create(**test_data)
        url = reverse('query-result')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': test_data})

    def test_ping(self):
        """Проверка ответа на пинг"""
        url = reverse('query-ping')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Pong'})

    def test_get_history(self):
        """Проверка получения истории запросов."""
        QueryLog.objects.create(
            cadastral_number='12345678',
            latitude='50.0000',
            longitude='30.0000',
            response=True
        )
        QueryLog.objects.create(
            cadastral_number='87654321',
            latitude='40.0000',
            longitude='20.0000',
            response=False
        )
        url = reverse('query-history')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)