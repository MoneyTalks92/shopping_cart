from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Cart


@ensure_csrf_cookie
class ShoppingCart(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        name = data.get("product_name")
        price = data.get("product_price")
        quantity = data.get("product_quantity")

        product_data = {
            "product_name": name,
            "product_price": price,
            "product_quantity": quantity
        }

        cart = Cart.objects.create(**product_data)

        data = {"message": f"New item added to the Cart with id: {cart.id}"}

        return JsonResponse(data, status=201)
