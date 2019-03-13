from django.urls import path,include,re_path
from wood import views

urlpatterns = [
    path('home/', views.home),
    path('demo/', views.demo),
    path('page/', views.bad_page),
    re_path(r'(?P<year>[0-9]{4})/$', views.year_today),
    re_path(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_today),
    path('author_del/', views.delete_author)
]

