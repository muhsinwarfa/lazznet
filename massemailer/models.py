from django.db import models

# Create your models here.
class Mail(models.Model):
    receiver = models.TextField(max_length= 200, null=False, blank=False)

