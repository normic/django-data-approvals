# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView,
    TemplateView
)

from .models import (
    Approval,
)


class ApprovalIndexView(TemplateView):
    template_name = "approvals/index.html"


class ApprovalCreateView(CreateView):
    model = Approval
    fields = ['created_by', 'approvaldata', 'content_type']


class ApprovalDeleteView(DeleteView):
    model = Approval


class ApprovalDetailView(DetailView):
    model = Approval


class ApprovalUpdateView(UpdateView):
    model = Approval


class ApprovalListView(ListView):
    model = Approval
