from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Posts

# Create your views here.

class HomePageView(ListView):
    model = Posts
    template_name = "home.html"