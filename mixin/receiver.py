#! /usr/bin/env python
from kombu import Queue, Exchange, Connection
from kombu.mixins import ConsumerMixin

class Worker(ConsumerMixin):
    task_queue = Queue('mixin_queue', Exchange('mixin_exchange',type='direct'), 'mixin_demo')

    def __init__(self, connection):
        self.connection = connection

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=[self.task_queue],
                         accept=['json'],
                         callbacks=[self.on_task])]

    def on_task(self, task, message):
        print('Got task: {0!r}'.format(task))

        message.ack()

connection = Connection('amqp://guest:guest@localhost:5672//')
server = Worker(connection)
try:
        server.run()
except KeyboardInterrupt:
        pass
