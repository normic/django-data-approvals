# -*- coding: utf-8 -*-

from django.db import models

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
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
    FINISHED = 2

    APPROVAL_STATES = (
        (REQUESTED, _('Requested')),
        (ASSIGNED, _('Assigned')),
        (FINISHED, _('Finished')),
    )

    state = models.IntegerField(choices=APPROVAL_STATES, default=REQUESTED, editable=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True, related_name='creator')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    # Todo: make (optional) use of new JSONField which requires Django> 1.9 and Postgres >=9.4 and Psycopg2 >= 2.5.4
    approvaldata = JSONField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(null=True, blank=True)

    approver = models.ForeignKey(User, null=True, blank=True, related_name='approver')
    approved = models.NullBooleanField(null=True, blank=True, db_index=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    approved_reason = models.CharField(max_length=50, blank=True)

    class Meta(object):
        verbose_name = _('approval')
        verbose_name_plural = _('approvals')

    def __unicode__(self):
        return u'%d, %s, %s, %s' % (
            self.id,
            self.get_state_display(),
            self.content_type,
            self.object_id
        )

    def get_absolute_url(self):
        return reverse('approval-detail', kwargs={'pk': self.pk})

    def set_approver(self, approver_username):
        """
        This method assigns an Approval to an approver by setting the State to ASSIGNED and adding the approver.
        """
        try:
            _approver = User.objects.get(username=approver_username)
        except User.DoesNotExist as err:
            if not err.args:
                err.args = ('', )
            err.args += ("Given username {0} does not exist!".format(approver_username), )
            raise

        self.approver = _approver
        self.state = Approval.ASSIGNED
        self.save()

    def set_approved(self, approved, approver=None, reason=None):
        """
        Sets an Approval as approved or declined and the state to FINISHED.
        Ensures that only the given approver can act on this Approval.

        :param approved: True or False
        :param approver: The User who acts as approver, if None the already set approver is used.
        :param reason: An optional reason - usually used if approval will be False.
        """
        self.approved = approved
        if approver:
            try:
                _approver = User.objects.get(username=approver)
            except User.DoesNotExist as err:
                if not err.args:
                    err.args = ('',)
                err.args += ("Given approver {0} does not exist!".format(approver),)
                raise
            self.approver = _approver

        if reason:
            self.reason = reason

        self.state = Approval.FINISHED
        self.save()


