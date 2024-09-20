from django.urls import path
from .views import ProductList
from ..project.urls import urlpatterns

urlpatterns = [path('', ProductList.as_view()),]