from django.db import models

# Create your models here.
class newss(models.Model):
    headline=models.CharField(max_length=200)
    desc=models.TextField()
    date=models.DateField()