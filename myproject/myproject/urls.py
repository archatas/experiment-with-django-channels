# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from clock.views import clock

urlpatterns = [
    url(r'^$', clock, name='clock'),
]
