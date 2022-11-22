from rest_framework.serializers import ModelSerializer
from .models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
