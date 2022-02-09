from django.db import models
from django.urls import reverse
from datetime import date


VALUES=(
    ('F','Five Cents'),
    ('E','Eight Cents'),
    ('T','Ten Cents')
)

# Create your models here.
class Stamp(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.TextField(max_length=230)
    country=models.CharField(max_length=100,default='China')
    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return reverse('detail', kwargs={'stampid': self.id})
    def collected_for_today(self):
          return self.feature_set.filter(date=date.today()).count() > 0

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