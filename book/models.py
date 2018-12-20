from django.db import models

from django.utils.timezone import now # import time now
# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=100)
    published_date=models.DateField(default=now)
    author=models.CharField(max_length=100)
    created_date=models.DateTimeField(auto_now=True) #ini adalah untuk insert auto data create date

    def __str__(self):
        return self.title



