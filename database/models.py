from django.db import models

class deal(models.Model):
    customers = models.CharField(max_length=120)
    item = models.CharField(max_length=120)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField()

# Create your models here.
