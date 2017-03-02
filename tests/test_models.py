#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-data-approvals
------------

Tests for `django-data-approvals` models module.
"""

from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from approvals.models import Approval


class TestApprovals(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the TestCase
        cls.user = User.objects.create_user(
            username='testuser', email='testuser@...', password='secret'
        )

        # set the User model as content_type
        user_ct = ContentType.objects.get_for_model(cls.user)

        approval = Approval.objects.create(
            state=Approval.REQUESTED,
            created_by=cls.user,
            content_type=user_ct
        )

    def test_retrieve(self):
        a = Approval.objects.get(pk=1)
        self.assertTrue(isinstance(a, Approval))
        self.assertEqual(a.__unicode__(), u'%d, %s, %s, %s' % (
            a.id,
            a.get_state_display(),
            a.content_type,
            a.object_id
        ))

    def test_set_approver(self):
        a = Approval.objects.get(pk=1)
        a.set_approver(self.user)
        self.assertEqual(a.state, Approval.ASSIGNED, "set_Approver didn't set correct state.")
        self.assertEqual(a.approver, self.user, "set_approver didn't set correct user.")

    def test_set_approved_true(self):
        a = Approval.objects.get(pk=1)
        a.set_approved(approved=True)
        self.assertEqual(a.state, Approval.FINISHED, "expected state FINISHED, but got {0}".format(a.state))
        self.assertEqual(a.approved, True, "expected value True, but got {0}".format(a.approved))

    def test_set_approved_false_missing_reason(self):
        a = Approval.objects.get(pk=1)
        self.assertRaises(ValueError, a.set_approved, approved=False)

    def test_set_approved_false(self):
        a = Approval.objects.get(pk=1)
        a.set_approved(approved=False, reason='Testreason')
        self.assertEqual(a.state, Approval.FINISHED, "expected state FINISHED, but got {0}".format(a.state))
        self.assertEqual(a.approved_reason, 'Testreason', "did not get expected reason")
        self.assertEqual(a.approved, False, "expected value False, but got {0}".format(a.approved))

    def tearDown(self):
        pass
