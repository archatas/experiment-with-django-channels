# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import json

from django.utils import timezone

from channels import Group
from channels.auth import channel_session

@channel_session
def ws_clock_connect(message):
    Group('clock-group').add(message.reply_channel)
    # first time value, the others will come from a management command
    Group('clock-group').send({
        'text': json.dumps({
            'time': timezone.localtime(timezone.now()).strftime("%H:%M:%S"),
        })
    })

@channel_session
def ws_clock_receive(message):
    data_sent = json.loads(message.content['text'])
    if 'color' in data_sent:
        Group('clock-group').send({
            'text': json.dumps({
                'color': data_sent['color'],
            })
        })

@channel_session
def ws_clock_disconnect(message):
    Group('clock-group').discard(message.reply_channel)
