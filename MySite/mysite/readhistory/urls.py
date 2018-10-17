from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'write', views.write, name='write'),
    url(r'login', views.login, name='login'),
    url(r'read', views.read, name='read'),
    url(r'test', views.test, name='test'),
    url(r'^myhistory', views.myhistory, name='myhistory'),
]
