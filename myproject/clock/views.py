# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def clock(request):
    return render(request, "clock/clock.html")
