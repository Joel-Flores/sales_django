from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=25, null=False)
    nit = models.IntegerField(null=False, default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default = True)

class Receipts(models.Model):
    sale_total = models.FloatField(null=False)
    received = models.FloatField(null=False)
    change = models.FloatField(null=False)
    client = models.ForeignKey(Clients, null=True, blank=True, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default = True)