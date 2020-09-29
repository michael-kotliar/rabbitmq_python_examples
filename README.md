

## Start RabbitMQ

You should specify `-h/--hostname` explicitly so that you don't get a random hostname. RabbitMQ stores data based on what it calls the "Node Name", which defaults to the hostname.
```
docker run \
    --rm \
    -ti \
    --hostname myrabbit \
    -p 15672:15672 \
    -p 5672:5672 \
    -e RABBITMQ_DEFAULT_USER=user \
    -e RABBITMQ_DEFAULT_PASS=password \
rabbitmq:3.8.9-management
```

