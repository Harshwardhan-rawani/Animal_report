from django.db import models

# Create your models here.
class feedback(models.Model):
    CustomerId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    feedback=models.TextField()
