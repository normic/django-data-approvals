# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy

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
    success_url = reverse_lazy('approvals:approval_list')


class ApprovalDetailView(DetailView):
    model = Approval


class ApprovalUpdateView(UpdateView):
    model = Approval
    fields = ['approvaldata', 'content_type']


class ApprovalListView(ListView):
    model = Approval
