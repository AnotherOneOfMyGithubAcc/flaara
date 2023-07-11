from django.db import models

# Create your models here.

# 1. Name 2. Restaurant name 3. Restaurant contact number 4. Cell phone 5. email 6. Restaurant address 7. Organization (restaurant)

class UserModel(models.Model):
    firstname = models.CharField(default="___", max_length=100)
    lastname = models.CharField(default="___", max_length=100)
    r_name = models.CharField(default="___", max_length=100)
    r_number = models.CharField(default="___", max_length=100)
    r_address = models.CharField(default="___", max_length=100)
    phone = models.CharField(default="___", max_length=100)
    email = models.EmailField()

