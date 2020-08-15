# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def intro(request):
    my_d = {'about_me' : "hi kartik here i am a CS guy..."}
    return render(request,'index1.html',context=my_d)
