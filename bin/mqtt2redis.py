#!/usr/bin/python

#Kwh per weekday

import time
import logging
import calendar
from datetime import datetime

import redis
import mosquitto

PREFIX = 'hellea'

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
log = logging

r = redis.StrictRedis()

class PowerCollector(object):
    def __init__(self, server):
        self.server = server
        self.client = mosquitto.Mosquitto()
        self.client.connect(server)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.subscribe('%s/#' % PREFIX)

    def on_connect(self, mosq, obj, msg):
        log.info('Connected to MQTT server: %s', self.server)

    def run(self):
        while True:
            try:
                if self.client.loop() != 0:
                    log.warning('Disonnected from MQTT server: %s', self.server)
                    self.__init__(self.server)
            except KeyboardInterrupt:
                self.client.disconnect()
                break

    def on_message(self, mosq, obj, msg):
        log.debug('%s : %s', msg.topic, str(msg.payload))
        topic = msg.topic.partition('/')[2]
        log.debug('filtered topic (1st pass): %s', topic)
        now = datetime.utcnow()
        category, s, topic = topic.partition('/')
        log.debug('filtered topic (2nd pass): %s', topic)
        bits = topic.split('/')
        if bits[0] == 'meter':
            meter = bits[1]
            if bits[2] == 'usage':
                    #log.debug('Meter %s incremented: %s' % (meter, msg.payload))
                    r.incrbyfloat('%s:power:%s:%s' % (PREFIX, meter, now.strftime('%Y-%m-%dT%H')), msg.payload)
                    r.incrbyfloat('%s:power:%s:%s' % (PREFIX, meter, now.strftime('%Y-%m-%d')), msg.payload)
                    r.incrbyfloat('%s:power:%s:%s' % (PREFIX, meter, now.strftime('%Y-%m')), msg.payload)
            if bits[2] == 'current':
                    timestamp = calendar.timegm(time.localtime())
                    r.zadd('%s:power:%s' % (PREFIX, meter), timestamp, '%s %s' % (timestamp, msg.payload))
                    log.info('Meter %s current usage: %s' % (meter, msg.payload))

if __name__ == '__main__':
    c = PowerCollector('mqtt.broker.local')
    c.run()
