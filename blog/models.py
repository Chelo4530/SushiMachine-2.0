from django.db import models
from django.utils import timezone


class Post(models.Model):
    nombre = models.CharField(max_length=180)
    sushi = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    direccion = models.CharField(max_length=220)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.sushi