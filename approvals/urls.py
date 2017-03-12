# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex="^$", view=views.ApprovalIndexView.as_view(), name='index'),
    url(
        regex="^approval/create/$",
        view=views.ApprovalCreateView.as_view(),
        name='approval_create',
    ),
    url(
        regex="^approval/(?P<pk>\d+)/delete/$",
        view=views.ApprovalDeleteView.as_view(),
        name='approval_delete',
    ),
    url(
        regex="^approval/(?P<pk>\d+)/$",
        view=views.ApprovalDetailView.as_view(),
        name='approval_detail',
    ),
    url(
        regex="^approval/(?P<pk>\d+)/update/$",
        view=views.ApprovalUpdateView.as_view(),
        name='approval_update',
    ),
    url(
        regex="^approval/$",
        view=views.ApprovalListView.as_view(),
        name='approval_list',
    ),
]
