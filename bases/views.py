from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from django.contrib.auth.mixins import  LoginRequiredMixin

class Home(LoginRequiredMixin,TemplateView):
    template_name="bases/home.html"
    login_url='config:login'