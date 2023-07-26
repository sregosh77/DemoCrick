from django.db import models

class Cricketers (models.Model):
    objects = None
    name = models.CharField(max_length=250)
    skill = models.TextField()
    year = models.IntegerField()
    img = models.ImageField ( upload_to= 'gallery')


    def __str__(self):
        return self.name



