from django.db import models

from receipts.models import Receipts
from product.models import ProductName
# Create your models here.
class Sales(models.Model):
    receipt = models.ForeignKey(Receipts, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductName, null=True, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    price_total = models.FloatField(null=False)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default = True)