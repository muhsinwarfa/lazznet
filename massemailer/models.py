from django.db import models
from django.core.validators  import RegexValidator
# Create your models here.
class Mail(models.Model):
    receiver = models.CharField(max_length=100)
    replymail = models.CharField(max_length=100,null=True, blank=True)
    pdf = models.FileField(upload_to='media/',null=True, blank=True)
    subject =  models.CharField(max_length=100)
    body =  models.TextField(default = "Hello",null=False, blank=False)


class Scrapper(models.Model):
    csvdump = models.TextField(default = "insert website",null=False, blank=False,
    )



