#! /usr/bin/env python
from __future__ import absolute_import, unicode_literals, print_function
from kombu import Connection, Exchange, Queue, Consumer, eventloop

exchange = Exchange('kombu_demo', type='direct')
queue = Queue('kombu_demo', exchange, routing_key='kombu_demo')

def handle_message(body, message):
    print('Received message: {0!r}'.format(body))
    message.ack()

with Connection('amqp://guest:guest@localhost:5672//') as connection:
    with Consumer(connection, queue, callbacks=[handle_message]):
        for _ in eventloop(connection):
            pass
