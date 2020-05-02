from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.FloatField()
