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
channel.queue_declare(queue="test", durable=True, exclusive=False, auto_delete=False)

def callback(ch, method, properties, body):
    print("Received:\t{0}".format(body.decode()))

channel.basic_consume(callback, queue="test", no_ack=True)
channel.start_consuming()
