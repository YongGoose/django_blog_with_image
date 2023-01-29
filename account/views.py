from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def test(request):
    print("정상 영업합니다.")

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('blog_views')
    return render(request, 'signup.html')