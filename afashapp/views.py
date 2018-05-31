from django.shortcuts import render

# Create your views here.
from .models import Post

# def post_list(request):
    # post_list = Post.objects.all()
def hello() :
    text = "hello world!"
    return render('index.html', 'text' = text)
