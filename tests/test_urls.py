#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `django-data-approvals` urls.
"""

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.test import TestCase

from approvals.models import Approval


class TestURLs(TestCase):

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

    def test_index(self):
        url = reverse('approvals:index', args=[])
        self.assertEqual(url, '/approvals/')

    def test_create(self):
        url = reverse('approvals:approval_create')
        self.assertEqual(url, '/approvals/approval/create/')

    def test_detail(self):
        url = reverse('approvals:approval_detail', kwargs={'pk': 1})
        self.assertEqual(url, '/approvals/approval/1/')

    def test_update(self):
        url = reverse('approvals:approval_update', kwargs={'pk': 1})
        self.assertEqual(url, '/approvals/approval/1/update/')

    def test_list(self):
        url = reverse('approvals:approval_list')
        self.assertEqual(url, '/approvals/approval/')

    def test_delete(self):
        url = reverse('approvals:approval_delete', kwargs={'pk': 1})
        self.assertEqual(url, '/approvals/approval/1/delete/')
