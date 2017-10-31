#coding:utf-8
from django.db import models

# Create your models here.
class Daily(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily'


class Duanzi(models.Model):
    question = models.CharField(max_length=200, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    answer = models.CharField(max_length=5000, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'duanzi'
