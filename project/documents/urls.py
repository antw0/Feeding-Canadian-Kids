from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'documents'

urlpatterns = [
    url(r'^$', views.index, name='index')
]