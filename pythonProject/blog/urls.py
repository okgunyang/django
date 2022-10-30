from django.urls import path
from . import views

urlpatterns = [
    # 작성예제
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]