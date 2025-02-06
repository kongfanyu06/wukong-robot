import asyncio
import errno
import functools
import socket

import tornado.ioloop
from tornado.iostream import IOStream
handlers = [
        tornado.web.URLSpec(
            r'/config',
            _ConfigHandler
        ),
        tornado.web.URLSpec(
            r'/health',
            _HealthHandler,
            {
                'service_state': service_state
            }
        ),
        tornado.web.URLSpec(
            r'/shutdown',
            _ShutdownHandler,
            {
                'service_state': service_state
            }
        ),
        tornado.web.URLSpec(
            r'/status',
            relayserver.StatusHandler,
            {
                'relay_server': relay_server,
                'stats': stats
            }
        )
    ]

    app = tornado.web.Application(
        handlers
    )
server = app.listen(
        tornado.options.options.private_port,
        tornado.options.options.private_address,
        xheaders=True,
        max_body_size=tornado.options.options.max_body_size,
        idle_connection_timeout=tornado.options.options.idle_timeout
    )