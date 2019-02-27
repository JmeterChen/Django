from django.urls import path,include,re_path
from index import views

urlpatterns = [
    path('login/', views.login),
    path('is_login/', views.is_login),
    path('bugs/', views.bugs_num),
    path('current/',views.current_date),
    path('app_current/',views.app_current_date),
    path('time/',views.now_time),
    # 这里是用正则表达式定义URL
    re_path(r'page/(\d+)/$',views.page_num)
]


