from celery import shared_task
import requests

@shared_task
def send_email(email, total, name):
	requests.post("http://nginx/api/v1/emails/send/", data={
		"receiver": email,
		"subject": "Order Created",
		"body": "Hello %s, your order has been created. Total of: %s. Thanks" % (name, total)
	})
