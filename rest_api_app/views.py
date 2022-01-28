from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Cart


@method_decorator(csrf_exempt, name='dispatch')
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

        data = {
            "message":
            f"New item has been added to the Cart with id: {cart.id}"
        }

        return JsonResponse(data, status=201)

    def get(self, request):
        items = Cart.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'product_name': item.product_name,
                'product_price': item.product_price,
                'product_quantity': item.product_quantity,
            })

        data = {
            'items': items_data,
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCartUpdate(View):

    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = Cart.objects.get(id=item_id)
        item.product_quantity = data['product_quantity']
        item.save()

        data = {'message': f'Item {item_id} has been updated'}

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCartDelete(View):

    def delete(self, request, item_id):
        item = Cart.objects.get(id=item_id)
        item.delete()

        data = {'message': f'Item {item_id} has been deleted'}

        return JsonResponse(data)
