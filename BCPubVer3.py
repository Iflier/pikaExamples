#-*- coding: utf-8 -*-
"""
Dec:
Created on : 2017.09.22
Author : Iflier
"""
print(__doc__)

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# 使用自动分配的通道号创建一个channel
channel = connection.channel()

# 声明一个队列
channel.queue_declare(queue="test", durable=True, exclusive=False, auto_delete=False)
# channel.exchange_declare(exchange="test", exchange_type='direct')
# 打开传送确认模式
channel.confirm_delivery()

# 发送一个消息，如果发送成功返回True
for i in range(1, 101, 1):
    if channel.basic_publish(exchange="test", routing_key="test",
                             body="hello, money. This is {0:>+3,d}".format(i)):
        print("Messages publish was confirmed.")
    else:
        print("Messages could not be confirmed.")
channel.close()
connection.close()
