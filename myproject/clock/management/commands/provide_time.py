# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import json
from django.utils import timezone
from time import sleep
from django.core.management.base import BaseCommand
from channels import Group

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        while True:
            new_time = timezone.localtime(timezone.now()).strftime("%H:%M:%S")
            # self.stdout.write(new_time)
            Group('clock-group').send({
                'text': json.dumps({
                    'time': new_time,
                })
            })
            sleep(1)
