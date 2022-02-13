from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



VALUES=(
    ('F','Five Cents'),
    ('E','Eight Cents'),
    ('T','Ten Cents')
)

# Create your models here.
class Owner(models.Model):
    name=models.CharField(max_length=100)
    postcode=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse ('owners_detail',kwargs={'pk':self.id})


class Stamp(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.TextField(max_length=230)
    country=models.CharField(max_length=100,default='China')
    owners=models.ManyToManyField(Owner)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return reverse('detail', kwargs={'stamp_id': self.id})
 

class Feature(models.Model):
    date=models.DateField()
    value=models.CharField(
        max_length=1,
        choices=VALUES,
        default=VALUES[0][0]
        )
    stamp=models.ForeignKey(Stamp,on_delete=models.CASCADE)
    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_value_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    stamp = models.ForeignKey(Stamp, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.stamp_id} @{self.url}"