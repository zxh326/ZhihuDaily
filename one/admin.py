#coding:utf-8
from django.contrib import admin
from .models import Tuwen
# Register your models here.
class TuwenAdmin(admin.ModelAdmin):
	"""docstring for oneAdmin"""
	list_display = ('id','text_authors','content')
	list_filter = ['date']
admin.site.register(Tuwen,TuwenAdmin)