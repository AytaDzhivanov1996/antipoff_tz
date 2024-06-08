from django.db import models


class QueryLog(models.Model):
    cadastral_number = models.CharField(max_length=50, verbose_name="кадастровый_номер")
    latitude = models.CharField(max_length=20, verbose_name="широта")
    longitute = models.CharField(max_length=20, verbose_name="долгота")
    response = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
