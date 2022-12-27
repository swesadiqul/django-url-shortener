from django.db import models

# Create your models here.
from django.db import models
class URLShortener(models.Model):
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=15)


    class Meta:
        verbose_name_plural = "URL Shortener"
        ordering = ["-id"]

    def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"