# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^approval/create/$",
        view=views.ApprovalCreateView.as_view(),
        name='approval-create',
    ),
    url(
        regex="^approval/(?P<pk>\d+)/delete/$",
        view=views.ApprovalDeleteView.as_view(),
        name='approval-delete',
    ),
    url(
        regex="^approval/(?P<pk>\d+)/$",
        view=views.ApprovalDetailView.as_view(),
        name='approval-detail',
    ),
    url(
        regex="^approval/(?P<pk>\d+)/update/$",
        view=views.ApprovalUpdateView.as_view(),
        name='approval-update',
    ),
    url(
        regex="^approval/$",
        view=views.ApprovalListView.as_view(),
        name='approval-list',
    ),
]
