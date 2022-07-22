from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Topic(models.Model):

    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text  = models.CharField()
    date_added = models.DateField(auto_now_add=True)

    class meta:
        verbose_name_plural = "entries"
    
    def __str__(self):

        return f'{self.text[:50]}....'