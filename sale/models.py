from django.db import models

from datetime import datetime
# Create your models here.

def set_is_active_to_false():
        return False
    
class ProductType(models.Model):
    name = models.CharField(max_length = 40, null = False, unique = True)
    create = models.DateTimeField(default = datetime.now())
    update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default = True)
    
    def __str__(self) -> str:
        return self.name
    
class ProductName(models.Model):
    name = models.CharField(max_length = 40, null = False, unique = True)
    price = models.FloatField(null = False)
    create = models.DateTimeField(default = datetime.now())
    update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default = True)
    type = models.ForeignKey(ProductType, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name