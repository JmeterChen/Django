from django.urls import path,include,re_path
from index import views

urlpatterns = [
    path('login/', views.login),
    path('is_login/', views.is_login),
    path('bugs/', views.bugs_num),
    path('time/',views.now_time),
    # 这里是用正则表达式定义URL
    re_path(r'page/(\d+)/$',views.page_num)
]
