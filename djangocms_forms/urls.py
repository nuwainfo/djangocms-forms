# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import re_path

from .views import FormSubmission

urlpatterns = [
    re_path(r'^forms/submit/$', FormSubmission.as_view(), name='djangocms_forms_submissions'),
]
