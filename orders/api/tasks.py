from celery import shared_task
import requests

@shared_task
def send_email(email, total, name):
	requests.post("http://127.0.0.1:8002/emails/send/", data={
		"receiver": email,
		"subject": "Order Created",
		"body": "Hello %s, your order has been created. Total of: %s. Thanks" % (name, total)
	})
