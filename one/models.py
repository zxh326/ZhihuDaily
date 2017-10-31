#coding:utf-8
from django.db import models

# Create your models here.
class Tuwen(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)
    img_url = models.CharField(max_length=80, blank=True, null=True)
    picture_author = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    text_authors = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tuwen'
