from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
# Create your views here.
def blog_views(request):
    blogs = BLog.objects.all()
    # return render(request, 'home.html', {'blogs':blogs})
    return render(request,'home.html', {'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(BLog, pk= id)
    return render(request, 'detail.html', {'blog' : blog})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = BLog()
    new_blog.title = request.POST['title']
    new_blog.author = request.POST['author']
    new_blog.image = request.FILES['image']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('blog_views')