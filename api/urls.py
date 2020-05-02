from django.urls import path
from .views import ProductList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('products.json', ProductList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

