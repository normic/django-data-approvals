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
        return u'%s, %s, %s, %s' % (
            self.id,
            self.get_state_display(),
            self.content_type,
            self.object_id
        )

    def get_absolute_url(self):
        return reverse('approvals:approval_detail', kwargs={'pk': self.pk})

    @classmethod
    def create(cls, creator, approvaldata, approval_for_model, object_id=None, ip_address=None):
        """
        Convenience method which creates a new Approval entry
        :param creator: a User instance
        :param approvaldata: the data which should be approved as JSON
        :param approval_for_model: the related model where the approval belongs to
        :param object_id: the changable object ID or None if it's a new object
        :param ip_address: optional IP adress of the requesting User
        :return:
        """
        try:
            created_by = User.objects.get(username=creator)
        except User.DoesNotExist as err:
            if not err.args:
                err.args = ('', )
            err.args += ("Given username {0} does not exist!".format(creator), )
            raise

        ct = ContentType.objects.get_for_model(approval_for_model)
        new_approval = cls(created_by=created_by, approvaldata=approvaldata,
                           content_type=ct, object_id=object_id, ip_address=ip_address)
        new_approval.save()
        return new_approval

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
        Ensures that only a valid user can act on this Approval.

        :param approved: True or False
        :param approver: The User who acts as approver, if None the already set approver is used.
        :param reason: An optional reason, but mandatory if approved is False.
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

        if not approved and reason is None:
            raise ValueError("If approved is False, reason must not be None!")
        elif reason is not None:
            self.approved_reason = reason

        self.state = Approval.FINISHED
        self.save()
