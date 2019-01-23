import pika

# Establishing connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel() 

# Checking if queue exists
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print ("[x] Received %r" %body)

channel.basic_consume(callback, queue='hello', no_ack=True)

print ('[*] Waiting for meassages. To exit press CTRL+C')
channel.start_consuming()
