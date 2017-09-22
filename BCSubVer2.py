#-*- coding: utf-8 -*-
"""
Dec:
Created on : 2017.09.22
Author : Iflier
"""
print(__doc__)

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

def callback(chan, method_frame, properties, body):
    print("delivery tag: {0}\tchannel num: {1}\tReceived body: {2}".format(method_frame.delivery_tag, chan.channel_number, body.decode()))
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

channel.basic_consume(callback, queue="test", no_ack=False)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    print("Stoped.")
channel.close()
connection.close()
