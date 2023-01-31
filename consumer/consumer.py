import pika
from random import choice
import os


CAR_TYPE = ['eco', 'delux']
DRIVER_TYPE = ['taxi', 'uber']
amqp_url = os.environ['AMQP_URL']

driver = choice(DRIVER_TYPE)
car_type = choice(CAR_TYPE)

print(f'Driver -> {driver} | {car_type}')

connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
channel = connection.channel()

channel.exchange_declare(exchange=driver, exchange_type='topic')

result = channel.queue_declare('carona')
queue_name = result.method.queue

channel.queue_bind(
    exchange=driver, queue=queue_name, routing_key=car_type)


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()