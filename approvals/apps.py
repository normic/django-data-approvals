# -*- coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ApprovalsConfig(AppConfig):
    name = 'approvals'
    verbose_name = _('Data Approvals App')

    def ready(self):
        import approvals.signals
