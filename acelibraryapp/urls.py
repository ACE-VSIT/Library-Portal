from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.member_login, name='member_login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/tasks', views.tasks, name='tasks'),
    url(r'^home/resource', views.resource, name='resource'),
    url(r'^home/python', views.python, name='python'),

    #TODO : Add routes for other pages
]