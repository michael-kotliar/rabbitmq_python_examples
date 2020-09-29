import pika
import json

# First thing to do is establish a connection with RabbitMQ server
# and create a new channel

# A connection represents a real TCP connection to the message broker,
# whereas a channel is a virtual connection (AMQP connection) inside it.
# This way you can use as many (virtual) connections as you want inside
# your application without overloading the broker with TCP connections.

credentials = pika.PlainCredentials("user", "password")
parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    virtual_host="/",          # provides a way to segregate applications using the same RabbitMQ instance
    credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# create a queue
channel.queue_declare(queue="hello")

message = {
    "job": {},
    "cwl": {}
}

# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange
channel.basic_publish(
    exchange="",               # default exchange, always Direct type
    routing_key="hello",       # in this case it's a queue name, but can be pattern if Exchange type is topic
    body=json.dumps(message)   # should be serialized to string
)

print(f"Message sent \n{message}")

# Make sure the network buffers are flushed and our message is actually delivered to RabbitMQ
connection.close()