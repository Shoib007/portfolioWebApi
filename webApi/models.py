from django.db import models

# Create your models here.

class projectDB(models.Model):
    title = models.CharField(max_length=255, default='title')
    sTitle = models.CharField(max_length=255, default='subTitle')
    imageLink = models.URLField(max_length=200, null=False, default='https://')
    gitLink = models.URLField(max_length=200, null=False, default='https://')
    description = models.TextField(max_length=255, default='description')

