# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import RegisterForm


def index(request):
    return render(request, 'index.html')
