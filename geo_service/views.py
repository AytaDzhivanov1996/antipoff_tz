import time
import random

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

from geo_service.models import QueryLog
from geo_service.serializers import QueryLogSerializer, QueryLogCreateSerializer


class QueryLogViewset(viewsets.ModelViewSet):
    """Вьюсет для работы с запросом и ответом"""
    queryset = QueryLog.objects.all()
    serializer_class = QueryLogSerializer

    def list(self, request):
        """Блок просмотра списка запросов"""
        raise MethodNotAllowed('GET', detail='Method "GET" not allowed without lookup')

    def create(self, request):
        """Функция создания запроса"""
        serializer = QueryLogCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Эмуляция отправки запроса на внешний сервер
            time.sleep(random.randint(2, 60))  # Ожидание от 10 до 60 секунд
            response = random.choice([True, False])  # Случайный ответ (true или false)

            serializer.validated_data['response'] = response
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    @action(detail=False, methods=['get'])
    def result(self, request):
        """Получение последнего запроса с ответом"""
        queryset = QueryLog.objects.all().last()
        serializer = self.get_serializer(queryset)
        return Response({'message': serializer.data})
    
    @action(detail=False, methods=['get'])
    def ping(self, request):
        """Тест работы сервиса"""
        return Response({'message': 'Pong'})
    
    @action(detail=False, methods=['get'])
    def history(self, request):
        """Получение всех запросов и ответов на них"""
        queryset = QueryLog.objects.all()
        serializer = QueryLogSerializer(queryset, many=True)
        return Response(serializer.data)
    