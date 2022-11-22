from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class RingsCategory(models.Model):
    title = models.CharField(max_length=100)
    base_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class RingCard(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='rings/%y/%m/%d')
    body = RichTextField()
    price = models.IntegerField()
    sale_price = models.IntegerField()
    discount_price = models.BooleanField(default=False)

    def __str__(self):
        return self.title