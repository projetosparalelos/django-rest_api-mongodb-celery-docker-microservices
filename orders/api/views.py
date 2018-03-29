from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Order
from .tasks import send_email
import json
from django.core import serializers


# TODO: add here your API Views

@api_view(http_method_names=["POST"])
def add_order(request):
	print(request.data)
	total_price = 0
	order = Order()
	order.customer_name = request.data["customer_name"]
	order.customer_email = request.data["customer_email"]
	order.items = []
	#
	#
	#
	for product in request.data["products_id"]:
		print(product)
		response = requests.get("http://127.0.0.1:8001/products/fetch/?prod_id=%s" % product).json()
		print(response)
		total_price += float(response[0]["price"])
	#
		order.items.append({
			"item_name": response[0]["name"],
			"item_description": response[0]["description"],
			"item_price": response[0]["price"],
		})
	order.total = total_price
	# order_json = json.dumps(order.__dict__)
	#
	send_email.delay(email=order.customer_email, total=order.total, name=order.customer_name)

	return Response({"message": "Order successfully created! You'll get email soon"})


