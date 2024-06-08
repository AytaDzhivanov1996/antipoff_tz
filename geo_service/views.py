import time
import random

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from geo_service.models import QueryLog
from geo_service.serializers import QueryLogSerializer


class QueryLogViewset(viewsets.ModelViewSet):
    queryset = QueryLog.objects.all()
    serializer_class = QueryLogSerializer

    def create(self, request):
        serializer = QueryLogSerializer(data=request.data)
        if serializer.is_valid():
            time.sleep(random.randint(10, 60))
            response = random.choice([True, False])

            serializer.validated_data['response'] = response
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def result(self, request):
        return Response({'message': 'Result received'})
    
    @action(detail=False, methods=['get'])
    def ping(self, request):
        return Response({'message': 'Pong'})
    
    @action(detail=False, methods=['get'])
    def history(self, request):
        queryset = QueryLog.objects.all()
        serializer = QueryLogSerializer(queryset, many=True)
        return Response(serializer.data)