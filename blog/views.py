from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post

post_list = ListView.as_view(model=Post)

post_detail = DeleteView.as_view(model=Post)
