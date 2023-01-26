"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.blog_views, name='blog_views'),
    path('<str:id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

 

# static과 settings를 임포트해주고, 기존의 urlpatterns에 settings.py에서 정의한 미디어 경로를 추가한다.

# 이렇게 코드를 추가함으로써 이미지는 테이블 속성 값으로 이미지 자체로 저장되어있는 것이 아닌 '/media/이미지이름.png' 처럼 path가 저장된다.

# 맨 아래 코드가 추가 코드임.