# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from approvals.urls import urlpatterns as approvals_urls

urlpatterns = [
    url(r'approvals/', include(approvals_urls, namespace='approvals')),
]
