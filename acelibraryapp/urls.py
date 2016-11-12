from django.conf.urls import url
from . import views
from acelibraryapp.views import TaskView,Authentication, HomePage
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$',(Authentication.as_view()),name='index'),
    #url(r'^$', views.member_login, name='member_login'),
    #url(r'^home/$', views.home, name='home'),
    url(r'^home/$',login_required(login_url='/')(HomePage.as_view()),name='home'),
    #url(r'^home/tasks', views.tasks, name='tasks'),
    url(r'^home/tasks',login_required(login_url='/')(TaskView.as_view()),name='tasks'),
    url(r'^home/resource', views.resource, name='resource'),
    url(r'^home/python', views.python, name='python'),


    #TODO : Add routes for other pages
]