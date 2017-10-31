# coding:utf-8
import json
from django.shortcuts import render
from zhihu.getdetail import run, getrandid, getToday
from django.http import HttpResponse
# Create your views here.


def dailydetail(request):
    request.encoding = 'utf-8'
    if 'date' in request.GET:
        body = run(request.GET['date'])
    elif 'date' in request.POST:
        body = run(request.POST['date'])
    else:
        body = '{\'ms\':400}'
    # return HttpResponse(body)

    return HttpResponse(json.dumps(body), content_type="application/json")


def dailyrandom(request):
    request.encoding = 'utf-8'
    if 'count' in request.GET:
        body = getrandid(request.GET['count'])
    elif 'count' in request.POST:
        body = getrandid(request.POST['count'])
    else:
        body = getrandid()

    return HttpResponse(json.dumps(body), content_type="application/json")


def getTodayDaily(request):
    request.encoding = 'utf-8'
    body = getToday()

    return HttpResponse(json.dumps(body), content_type="application/json")


def home(request):
    return HttpResponse('It\'s work! ')
