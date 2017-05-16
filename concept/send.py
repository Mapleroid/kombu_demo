#! /usr/bin/env python
from __future__ import absolute_import, unicode_literals
from kombu import Connection, Producer, Exchange

exchange = Exchange('kombu_demo', type='direct')

with Connection('amqp://guest:guest@localhost:5672//') as connection:
    producer = Producer(connection)
    producer.publish({'hello': 'world'},
                     exchange=exchange,
                     routing_key='kombu_demo',
                     serializer='json', compression='zlib')
