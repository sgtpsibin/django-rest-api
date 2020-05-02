from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
# Create your views here.


class ProductList(APIView):
    
    def get(self, request):
        data = Product.objects.all()     
        serialized = ProductSerializer(data, many=True)
        return Response({'products': serialized.data})



    def post(seft, request):
        return Response({'products': request.data})