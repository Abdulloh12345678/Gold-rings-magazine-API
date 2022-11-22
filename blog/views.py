from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
# from rest_framework import status
from .models import *
from .serializer import *
# Create your views here.
class CategoryApiView(APIView):
    def get(self, request):
        category = Category.objects.all()
        obj = CategorySerializer(category, many=True)
        return Response(obj.data)

class BannerApiView(APIView):
    def get(self, request):
        banner = Banner.objects.all()
        obj = BannerSerializer(banner, many=True)
        return Response(obj.data)
        
class BrandApiView(APIView):
    def get(self, request):
        brand = Brand.objects.all()
        obj = BrandSerializer(brand, many=True)
        return Response(obj.data)

class DiscountApiView(APIView):
    def get(self, request):
        discount = Discount.objects.order_by('-id').all()
        obj = DiscountPageSerializer(discount, many=True)
        return Response(obj.data)

class VideoApiView(APIView):
    def get(self, request):
        video = Video.objects.all()
        obj = VideoSerializer(video, many=True)
        return Response(obj.data)

class ProductApiView(APIView):
    def get(self, request):
        products = Products.objects.all()
        obj = ProductSerializer(products, many=True)
        return Response(obj.data)

class CatalogApiView(APIView):
    def get(self, request):
        catalog = Catalog.objects.all()
        obj = CatalogSerializer(catalog, many=True)
        return Response(obj.data)