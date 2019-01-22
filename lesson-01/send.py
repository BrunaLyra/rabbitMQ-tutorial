import pika

# Establishing connection with RabbitMQ server

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.chanel() 

# Checking if queue exists
channel.queue_declare(queue='hello')

# Send message and close connection
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
