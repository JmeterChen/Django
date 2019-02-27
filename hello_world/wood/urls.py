from django.urls import path,include,re_path
from index import views

urlpatterns = [
    path('home/', views.home),

]

