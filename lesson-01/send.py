import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.chanel() 
