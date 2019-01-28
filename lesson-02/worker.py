import pika
import time

# Establishing connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel() 

# Making sure queue exists and marking as durable
channel.queue_declare(queue='task_queue',durable=True)

# Callback function
def callback(ch, method, properties, body):
    print ("[x] Received %r" %body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)   ## Send a manual ack

channel.basic_qos(prefetch_count=1) ## Fair dispatch
channel.basic_consume(callback, queue='task_queue')

print ('[*] Waiting for meassages. To exit press CTRL+C')
channel.start_consuming()
