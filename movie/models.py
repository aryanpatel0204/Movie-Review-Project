from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=400)
    image=models.ImageField(upload_to='movie/images/')
    url=models.URLField(blank=True)#optional

    def __str__(self):
        return self.title