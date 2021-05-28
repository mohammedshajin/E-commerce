from django.db import models
from django.utils.text import slugify
import uuid

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='assets')
    desc = models.TextField(max_length=500)
    slug = models.SlugField(max_length=255, unique=True, blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title + '-' + str(uuid.uuid4()))
        super(Product, self).save()

