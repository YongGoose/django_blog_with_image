from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django import forms



def validate_score(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists(): #아이디 중복 체크 
           raise ValidationError("아이디가 이미 사용중입니다.")