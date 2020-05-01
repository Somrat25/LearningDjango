from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    all_post = Post.objects.all()

    return render(request, 'index.html', {
        'name' : "Moshahed Somrat",
        'study' : "Northern University of Business & Technology , Khulna",
        'district' : "khulna",
        'all_post_list' : all_post
    })

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'post_list.html', {
        'post_list' : post_list
    })

def single_post(request):
    post = Post.objects.get(pk=1)
    return render(request, 'single_post.html',{
        'post': post
    })