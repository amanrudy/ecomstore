from django.contrib import admin
from django.urls import path, re_path
from .views import (
    show_cart
)

urlpatterns = [
	re_path(r'^show_cart/$', show_cart, name='show_cart'),
]

