from django.shortcuts import render
from  .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = "home.html"

class DetailPageView(DetailView):
    model = Post
    template_name = "detail.html"

class CreatePageView(CreateView):
    model = Post
    template_name = "create.html"
    fields = ["titulo","descripcion","autor"] 
    success_url =  reverse_lazy("home")
class DeletePageView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("home")   
