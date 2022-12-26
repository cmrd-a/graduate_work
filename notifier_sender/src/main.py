import json
import logging

import pika

from config import settings
from email_service import EmailService, EmailMessageParams

email_service = None


def send_email(ch, method, properties, body: bytes):
    message_params = EmailMessageParams(**json.loads(body))
    email_service.send_message(message_params)

    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(settings.rabbit_host))
    channel = connection.channel()

    result = channel.queue_declare(queue="email-channel.v1", durable=True)
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue=result.method.queue, on_message_callback=send_email)
    channel.start_consuming()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    email_service = EmailService()
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Graceful shutdown")
        email_service.server.close()
