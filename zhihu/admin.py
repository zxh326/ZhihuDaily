#coding:utf-8
from django.contrib import admin
from .models import Daily,Duanzi
# Register your models here.

class DailyAdmin(admin.ModelAdmin):
	"""docstring for Dailyadmin"""
	list_display = ('id','title','date')
	list_filter = ['date']

class DuanziAdmin(admin.ModelAdmin):
    list_display = ('question','answer','count')

admin.site.register(Duanzi,DuanziAdmin)
admin.site.register(Daily,DailyAdmin)
