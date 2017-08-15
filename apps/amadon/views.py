# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from time import gmtime, strftime
# Create your views here.

def index(request):
    if not 'list' in request.session:
        request.session['list'] = [
        {"name":"Dojo Tshirt","price":19.99},
        {"name":"Dojo Sweater","price":29.99},
        {"name":"Dojo Cup","price":4.99},
        {"name":"Algorithm Book","price":49.99}
        ]
    if not 'total' in request.session:
        request.session['total'] = 0
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request,'amadon/index.html')

def process(request):
    num = request.POST['price']
    request.session['total'] += request.session['list'][int(num)]['price']
    request.session['prev'] = request.session['list'][int(num)]['price']
    request.session['count'] += 1
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request,'amadon/checkout.html')