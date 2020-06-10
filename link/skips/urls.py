from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'[0-9a-zA-Z]/$', views.skip),
]