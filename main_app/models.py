from django.db import models

# Create your models here.
class Stamp(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.TextField(max_length=230)
    release_year=models.IntegerField()
    def __str__(self):
        return self.name
 
