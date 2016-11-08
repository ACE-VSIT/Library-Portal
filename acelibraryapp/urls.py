from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^login/', views.member_login, name='member_login'),
    url(r'^tasks/', views.showTasks, name='show_tasks'),
    url(r'^logout/$', views.member_logout, name='logout'),
    url(r'^fbLogin/$', views.facebook_login, name='facebook_login'),
    #TODO : Add routes for other pages
]