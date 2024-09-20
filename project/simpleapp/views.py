from django.views.generic import ListView
from .models import Product

class ProductList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    contex_object_name = 'products'


# Create your views here.
