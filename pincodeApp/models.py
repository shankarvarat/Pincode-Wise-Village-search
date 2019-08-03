from django.db import models

# Create your models here.
class pincode(models.Model):
    Village=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    StateName=models.CharField(max_length=50)
    def __str__(self):
        return self.Pincode