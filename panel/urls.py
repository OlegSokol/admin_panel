from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = 'panel'

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^my-orders/(?P<user_id>[0-9]+)$', views.MyOrdersView.as_view(), name='my_orders'),
    url(r'^(?P<order_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^(?P<order_id>[0-9]+)/update-status/$', views.update_status, name='update_status')
]
