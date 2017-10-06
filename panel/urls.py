from django.conf.urls import url
from . import views

app_name = 'panel'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<order_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^(?P<order_id>[0-9]+)/update-status/$', views.update_status, name='update_status')
]
