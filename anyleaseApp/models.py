from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, related_name = 'product', on_delete= CASCADE)
    description = models.CharField(max_length = 200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image_upload = models.URLField()
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['-date_created']

        def __str__(self):
            return self.name
