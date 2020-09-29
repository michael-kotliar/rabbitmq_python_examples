import pika, sys, os


def callback(ch, method, properties, body):
    print(f"Received message \n{body}")


def main():

    # need to connect to RabbitMQ server. The same way we did on sent.py
    credentials = pika.PlainCredentials("user", "password")
    parameters = pika.ConnectionParameters(
        host="localhost",
        port=5672,
        virtual_host="/",
        credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # we repeat creating a queue in case this code is run before sent.py
    channel.queue_declare(queue="hello")

    # to receive a message you need to subscribe to a queue and define callback
    channel.basic_consume(
        queue="hello",
        on_message_callback=callback,
        auto_ack=True
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)