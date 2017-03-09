# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from channels.routing import route

from clock.consumers import ws_clock_connect, ws_clock_receive, ws_clock_disconnect


channel_routing = [
    route('websocket.connect', ws_clock_connect, path=r'^/clock/$'),
    route('websocket.receive', ws_clock_receive, path=r'^/clock/$'),
    route('websocket.disconnect', ws_clock_disconnect, path=r'^/clock/$'),
    # here can be more routes with different paths
]
