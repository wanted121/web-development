from django.db import models

# Create your models here.
class Contect(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    quary=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
