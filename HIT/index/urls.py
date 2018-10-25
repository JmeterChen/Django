from django.conf.urls import url


urlpatterns = [
    url(r'^home/$', 'index.views.home'),
    url(r'^login/$', 'index.views.login'),
    url(r'^signup/$', 'index.views.signup'),
    url(r'^api/user_check/', 'index.views.user_check'),
    url(r'^api/login/$', 'index.views.api_login'),
    url(r'^api/search_task/$', 'index.views.search_task'),
    url(r'^api/new_task/$', 'index.views.api_task_new'),
    url(r'^task/list/$', 'index.views.task_list'),
    url(r'^task/new/$', 'index.views.task_new'),
]