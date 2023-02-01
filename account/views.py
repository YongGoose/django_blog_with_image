from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django import forms
from .validator import validate_score

# Create your views here.
def test(request):
    print("정상 영업합니다.")

def signup(request):
    # if request.method == 'POST':
    #     memo = forms.CharField(max_length=80, validators= [validate_score])
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists(): #아이디 중복 체크 
           raise ValidationError("아이디가 이미 사용중입니다.")
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            print("username")
            return redirect('blog_views')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            print("12345")
            return redirect('blog_views')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('blog_views')