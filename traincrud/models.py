from django.db import models
from django.db.models import Model



class Train(models.Model):

    TrainImage = models.ImageField(upload_to ='images/')

