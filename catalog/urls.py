from django.contrib import admin
from django.urls import path, re_path
from .views import (
    index,
    show_category,
    show_product
)

urlpatterns = [
	re_path(r'^$', index, name='catalog_home'),
	re_path(r'^category/(?P<category_slug>[-\w]+)/$', show_category, name='catalog_category'),
	re_path(r'^product/(?P<product_slug>[-\w]+)/$', show_product, name='catalog_product'),
]



# urlpatterns = patterns('ecomstore.catalog.views',
# (r'^$', 'index', { 'template_name':'catalog/index.html'}, 'catalog_home'),

# (r'^category/(?P<category_slug>[-\w]+)/$', 
# 'show_category', {
# 'template_name':'catalog/category.html'},'catalog_category'),

# (r'^product/(?P<product_slug>[-\w]+)/$', 
# 'show_product', {
# 'template_name':'catalog/product.html'},'catalog_product'),
# )