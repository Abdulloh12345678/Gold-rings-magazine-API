from django.db import models
# Create your models here.
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner/%y/%m/%d')
    chegirmalar = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=10, blank=True,)
    image = models.ImageField(upload_to='Brand/%y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Video(models.Model):
    video = EmbedVideoField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.video

class GoldSize(models.Model):
    price = models.PositiveIntegerField()
    count = models.IntegerField()
    base_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Material(models.Model):
    title = models.CharField(max_length=100)
    slug =models.SlugField(unique=True)    

    def __str__(self):
        return self.title

class ExtraMaterial(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)    
    material = models.ManyToManyField(Material)

    def __str__(self):
        return self.title

class Discount(models.Model):
    title = models.CharField(max_length=10,blank=True)
    percent_sale = models.PositiveIntegerField()
    new_rings =  models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now=True)
    material = models.ManyToManyField(ExtraMaterial,)
    
    def __str__(self):
        return self.title

class Detail(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='detail/%y/%m/%d')
    price = models.PositiveIntegerField()
    size = models.ManyToManyField(GoldSize)

    def __str__(self):
        return self.title

class Products(models.Model):
    body = RichTextField()
    image = models.ImageField(upload_to='NewProduct/%y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now=True)
    detail = models.ManyToManyField(Detail,)   
    materials = models.ManyToManyField(Material, )
    price = models.IntegerField(null=True)
    sale_price = models.IntegerField(null=True)
    discount_percent = models.ManyToManyField(Discount,)
    
    def __str__(self):
        return self.body
