from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item_num = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200, null=True, blank=False)
    quantity = models.IntegerField(max_length=2, null=True, blank=True)
    in_basket = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.item_name

    class Meta:
        ordering = ['in_basket']
