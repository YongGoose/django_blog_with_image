from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"
urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'), # 코드 추가하기
    path('signup', views.signup, name='signup')
]