from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to="img%y", null=True)

    def __str__(self):
        return self.name

