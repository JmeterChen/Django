from django.urls import path,include,re_path
from wood import views

urlpatterns = [
    path('home/', views.home),
]

