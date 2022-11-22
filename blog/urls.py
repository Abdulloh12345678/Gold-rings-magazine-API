from django.urls import path
from . import views

urlpatterns = [
     path('category/', views.CategoryApiView.as_view(), name='category'),           
     path('banner/', views.BannerApiView.as_view(), name='banner'),           
     path('brand/', views.BrandApiView.as_view(), name='brand'),           
     path('video/', views.VideoApiView.as_view(), name='video'),           
     path('products/', views.ProductApiView.as_view(), name='new_products'),           
     path('catalog/', views.CatalogApiView.as_view(), name='catalog'),           
]