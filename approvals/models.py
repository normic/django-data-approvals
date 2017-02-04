# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext_lazy as _

from annoying.fields import JSONField


class Approval(models.Model):
    """
    Describes an object which is requested for change or add.
    Usually this request comes from a user and/or a frontend application.

    Each entry contains one record of a change/add request related to a model.
    """

    REQUESTED = 0
    ASSIGNED = 1
    APPROVED = 2
    DECLINED = 3

    APPROVAL_STATES = (
        (REQUESTED, _('Requested')),
        (ASSIGNED, _('Assigned')),
        (APPROVED, _('Approved')),
        (DECLINED, _('Declined')),
    )

    approvalstate = models.IntegerField(choices=APPROVAL_STATES, default=REQUESTED)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True, related_name='creator')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    # Todo: make (optional) use of new JSONField which requires Django> 1.9 and Postgres >=9.4 and Psycopg2 >= 2.5.4
    approvaldata = JSONField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(null=True, blank=True)

    approval_at = models.DateTimeField(null=True, blank=True)
    approval_by = models.ForeignKey(
        User, null=True, blank=True, related_name='approver')
    approval_reason = models.CharField(max_length=50, blank=True)

    class Meta(object):
        verbose_name = _('approval')
        verbose_name_plural = _('approvals')

    def __unicode__(self):
        return u'%d, %s, %s, %s' % (
            self.id,
            self.get_approvalstate_display(),
            self.content_type,
            self.object_id
        )
