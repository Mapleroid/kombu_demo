#! /usr/bin/env python
from __future__ import absolute_import, unicode_literals
from kombu import Connection, Producer, Exchange

exchange = Exchange('mixin_exchange', type='direct')

with Connection('amqp://guest:guest@localhost:5672//') as connection:
    producer = Producer(connection)
    producer.publish({'hello':'work'},
                     exchange=exchange,
                     routing_key='mixin_demo',
                     serializer='json',
                     compression='zlib')
