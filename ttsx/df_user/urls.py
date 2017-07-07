from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^register_check/$', views.register_check),
    url(r'^check_user_name/$', views.check_user_name),
    url(r'^login_check/$', views.login_check),
    url(r'^user_center_info/$', views.user_center_info),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^user_center_site/$', views.user_center_site),
    url(r'^logout/$', views.logout),
]
