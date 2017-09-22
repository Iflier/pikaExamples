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

for method, properties, body in channel.consume("test"):
    print("delivery tag: {0}\tbody: {1}".format(method.delivery_tag, body.decode()))
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if method.delivery_tag == 100:
        break
requeueMessages = channel.cancel()
print("Requeued {0} messages.".format(requeueMessages))

channel.close()
connection.close()
