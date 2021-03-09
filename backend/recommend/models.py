from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    ISBN = models.CharField(max_length=13)
    DDC = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Meal(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)
    category = models.CharField(max_length=10, blank = True, null = True)
    instructions = models.CharField(max_length=4000, blank = True, null = True)
    region = models.CharField(max_length=20, blank = True, null = True)
    slug = models.SlugField(default = 'test')
    image_url = models.CharField( max_length=50, blank = True, null = True)

    def __str__(self):
        return self.name