import pika
import sys

# Establishing connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel() 

# Making sure queue exists and marking as durable
channel.queue_declare(queue='task_queue', durable=True)


# Send message and close connection
message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2, ## making message persistent
                      ))
print(" [x] Sent %r" % message)

connection.close()
