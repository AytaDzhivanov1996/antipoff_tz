from rest_framework import serializers

from geo_service.models import QueryLog


class QueryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryLog
        fields = '__all__'