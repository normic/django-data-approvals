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
            approvalstate=Approval.REQUESTED,
            created_by=cls.user,
            content_type=user_ct
        )

    def test_retrieve(self):
        a = Approval.objects.get(pk=1)
        self.assertTrue(isinstance(a, Approval))
        self.assertEqual(a.__unicode__(), u'%d, %s, %s, %s' % (
            a.id,
            a.get_approvalstate_display(),
            a.content_type,
            a.object_id
        ))

    def tearDown(self):
        pass
