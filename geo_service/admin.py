from django.contrib import admin

from geo_service.models import QueryLog

#Дефолтная админка  Django
admin.site.register(QueryLog)
