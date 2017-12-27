from django.db import models
from django.utils import timezone

class Sentence(models.Model):
    author = models.CharField(max_length=2)
    email = models.EmailField(max_length=254)
    content = models.CharField(max_length=140)
    pub_date = models.DateTimeField(default=timezone.now)
