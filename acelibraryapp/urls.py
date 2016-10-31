from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^tasks/', views.Tasks, name='tasks'),
    url(r'^login/', views.member_login, name='member_login'),
]