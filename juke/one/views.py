#coding:utf-8
import json
from django.shortcuts import render
from django.http import HttpResponse

from .getdetail import run,getinfo
from one.models import Tuwen

# Create your views here.

def tuwen(request):
    if 'count' in request.GET:
        count = request.GET['count']
    else:
        count = 1

    if 'rand' in request.GET:
        rand = request.GET['rand']
    else:
        rand = 0
    body = run(count,rand)
    return HttpResponse(json.dumps(body), content_type="application/json")
