from django.db import models

# Create your models here.


class Link(models.Model):

    long_link = models.CharField(max_length=64)
    short_link = models.CharField(max_length=64)


