#Django native imports
#from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.urls import path
from django.views.generic import edit

# Import from our apps
from netdev import views


urlpatterns = [
    url(r'^router_list$', views.RouterList.as_view(), name='router_list'),
    url(r'^firewall_list$', views.FirewallList.as_view(), name='firewall_list'),
    url(r'^switch_list$', views.SwitchList.as_view(), name='switch_list'),
    url(r'^other_list$', views.OtherList.as_view(), name='other_list'),
    url(r'^juniper_list$', views.JuniperList.as_view(), name='juniper_list'),
    url(r'^fortigate_list$', views.FortigateList.as_view(), name='fortigate_list'),
    url(r'^other_devices_list$', views.OtherDevicesList.as_view(), name='other_devices_list'),
    url(r'^(?P<pk>\d+)/$', views.NetdevDetail.as_view(), name='netdev_detail'),
    ]
