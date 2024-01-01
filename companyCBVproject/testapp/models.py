from django.db import models
from django.urls import reverse

class Company(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=120)
    ceo=models.CharField(max_length=40)
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

