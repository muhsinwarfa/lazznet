from django.db import models

# Create your models here.
class Mail(models.Model):
    receiver = models.TextField(null=False, blank=False)
    subject =  models.CharField(max_length=100)
    body =  models.TextField(default = "Hello",null=False, blank=False)



