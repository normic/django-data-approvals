# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
    Approval,
)


class ApprovalCreateView(CreateView):
    model = Approval
    fields = ['state', 'created_by', 'ip_address', 'approvaldata', 'content_type']


class ApprovalDeleteView(DeleteView):
    model = Approval


class ApprovalDetailView(DetailView):
    model = Approval


class ApprovalUpdateView(UpdateView):
    model = Approval


class ApprovalListView(ListView):
    model = Approval
