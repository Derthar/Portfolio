from django.urls import path
from Products.views import *

app_name = 'Products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='index_category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove')

]


