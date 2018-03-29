from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

swagger_view = get_swagger_view(title='Your API')

API_PREFIX = r'api/v1'

urlpatterns = [
    path(f'{API_PREFIX}/docs/', swagger_view),
	path("private/categories/", views.categories),
	path("products/fetch/", views.products_fetch),
	path("products/create/", views.products_create),
	path("products/delete/", views.products_delete) ,
]
