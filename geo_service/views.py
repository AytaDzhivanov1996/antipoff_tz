import time
import random
from django.db import transaction

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from geo_service.models import QueryLog
from geo_service.serializers import QueryLogSerializer, QueryLogCreateSerializer


class QueryLogViewset(viewsets.ModelViewSet):
    queryset = QueryLog.objects.all()
    serializer_class = QueryLogSerializer

    def create(self, request):
        serializer = QueryLogCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Эмуляция отправки запроса на внешний сервер
            time.sleep(random.randint(1, 5))  # Ожидание от 10 до 60 секунд
            response = random.choice([True, False])  # Случайный ответ (true или false)

            serializer.validated_data['response'] = response
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    @action(detail=False, methods=['get'])
    def result(self, request):
        queryset = QueryLog.objects.all().last()
        serializer = self.get_serializer(queryset)
        return Response({'message': serializer.data})
    
    @action(detail=False, methods=['get'])
    def ping(self, request):
        return Response({'message': 'Pong'})
    
    @action(detail=False, methods=['get'])
    def history(self, request):
        queryset = QueryLog.objects.all()
        serializer = QueryLogSerializer(queryset, many=True)
        return Response(serializer.data)