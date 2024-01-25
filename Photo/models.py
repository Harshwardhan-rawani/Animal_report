from django.db import models

# Create your models here.
class photo(models.Model):
    Name=models.CharField(max_length=50)
    Photo=models.FileField(upload_to="image/",max_length=350,null=True,default=None)