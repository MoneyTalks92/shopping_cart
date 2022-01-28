from django.urls import path
from .views import ShoppingCart, ShoppingCartUpdate, ShoppingCartDelete

urlpatterns = [
    path('cart-items/', ShoppingCart.as_view()),
    path('update-item/<int:item_id>', ShoppingCartUpdate.as_view()),
    path('delete-item/<int:item_id>', ShoppingCartDelete.as_view())
]