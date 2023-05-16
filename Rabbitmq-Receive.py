
import pika
credentials = pika.PlainCredentials(username='admin', password='admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='srv1', port=5672, virtual_host='/', credentials=credentials))
ch2=connection.channel()
ch2.queue_declare(queue='hello')

#-------------------------------------------------------------------------------------------------
def callback(ch,method,properties,body):
    print(f'Received {body}')

ch2.basic_consume(queue='hello',on_message_callback=callback,auto_ack=True)
print("waiting for message to exit press ctrl+c")
ch2.start_consuming() 

##################################################################################################  OR

import pika
import time

credentials=pika.PlainCredentials(username='admin', password='admin')
connection=pika.BlockingConnection(pika.ConnectionParameters(host='srv1', port=5672, virtual_host='/', credentials=credentials))
ch=connection.channel()
ch.queue_declare(queue='first',durable=True)
print('waiting untill press ctl+c')


def callback(ch,method,properties,body): #in documentation  in publisher we can find properties
    print(f'Received {body}')
    #print(properties.headers)
    print(method)
    time.sleep(9)
    print('done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue='first',on_message_callback=callback)
ch.start_consuming()
