from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'Home/home.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'Home/about.html')


