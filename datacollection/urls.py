from django.conf.urls import url

from .views import (
    DrinksList,
    DataList,
    DataDetail
)


urlpatterns = [
    url(r'^drinks/$', DrinksList.as_view(), name='drinks_list'),
    url(r'^data_collected/$', DataList.as_view(), name='data_list'),
    url(r'^record/(?P<pk>[a-z0-9-]+)/$',
        DataDetail.as_view(), name='data_detail')
]
