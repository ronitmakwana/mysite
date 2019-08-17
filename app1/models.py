from django.db import models


# Create your models here.
class product(models.Model):
    p_name=models.CharField(max_length=20)
    p_price=models.IntegerField()

