
import pika
credentials = pika.PlainCredentials(username='admin', password='admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='srv1', port=5672, virtual_host='/', credentials=credentials))



ch1=connection.channel()

ch1.queue_declare(queue='hello')
ch1.basic_publish(exchange='',routing_key='hello',body='hello b1')
print("message sent")
connection.close()

#######################################################################################   OR

import pika
credentials=pika.PlainCredentials(username='admin', password='admin')
connection=pika.BlockingConnection(pika.ConnectionParameters(host='srv1', port=5672, virtual_host='/', credentials=credentials))
ch=connection.channel()
ch.queue_declare(queue='first',durable=True)#durable ==if server will restart the channels will save in hard
message='this is my testing channel'
ch.basic_publish(exchange='',routing_key='first',body=message,properties=pika.BasicProperties(delivery_mode=2))#delivery mode = persist or transient messages
#we can add headers here   ==> headers={'name':'vahid'}

print('sending message')
connection.close()
