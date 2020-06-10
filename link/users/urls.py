from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^linkchange/$', views.link_change.as_view(), name='linkchange'),
]