from django.shortcuts import render
from .models import *
# Create your views here.
def blog_views(request):
    blogs = BLog.objects.all()
    # return render(request, 'home.html', {'blogs':blogs})
    return render(request,'home.html', {'blogs':blogs})