from cart import cart
from django.shortcuts import render

# Create your views here.


def show_cart(request):
	cart_item_count = cart.cart_distinct_item_count(request)
	page_title = 'Shopping Cart'
	return render(request, 'cart/cart.html', locals())


