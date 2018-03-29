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
	customer_name = request.data["customer_name"]
	customer_email = request.data["customer_email"]
	items = []
	#
	#
	#
	for product in request.data["products_id"]:
		print(product)
		response = requests.get("http://nginx/api/v1/products/fetch/?prod_id=%s" % product).json()
		print(response)
		total_price += float(response[0]["price"])
	#
		items.append({
			"item_name": response[0]["name"],
			"item_description": response[0]["description"],
			"item_price": response[0]["price"],
		})

	new_order = Order.objects.create(customer_name=customer_name, customer_email=customer_email, items=items, total=total_price)
	# order_json = json.dumps(order.__dict__)
	#
	send_email.delay(email=customer_email, total=total_price, name=customer_name)

	return Response({"message": "Order successfully created! You'll get email soon"})


