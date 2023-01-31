import pika
import sys
import os
import time
import threading
from random import choice


CAR_TYPE = ['eco', 'delux']
DRIVER_TYPE = ['taxi', 'uber']
amqp_url = os.environ['AMQP_URL']

def publisher():
    for i in range(200):
        driver = choice(DRIVER_TYPE)
        car_type = choice(CAR_TYPE)
        print(f'Solicitando: {driver} -> {car_type}')
        connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
        channel = connection.channel()
        channel.queue_declare(queue='carona')
        channel.basic_publish(exchange=driver,
                                routing_key=f'{car_type}',
                                body=f'Preciso de um {driver} meu endereço é: ZZZZ'
                                )
        time.sleep(5)


if __name__ == '__main__':
    try:
        pub = threading.Thread(target=publisher)
        pub.start()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
