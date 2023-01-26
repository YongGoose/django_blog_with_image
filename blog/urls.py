from django.urls import path
from . import views
urlpatterns =[  
    path('',views.blog_views, name='blog_views'),
    path('<str:id>', views.detail, name='detail'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('post/', views.make_post, name='post')
]