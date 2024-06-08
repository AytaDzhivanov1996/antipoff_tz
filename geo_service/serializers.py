from rest_framework import serializers

from geo_service.models import QueryLog


class QueryLogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = QueryLog
        exclude = ['id', 'response', 'created_at']


class QueryLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = QueryLog
        exclude = ['id', 'created_at']
