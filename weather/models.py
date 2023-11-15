from django.db import models

# Create your models here.
class meteoData(models.Model):
    # Define fields (attributes) for your model here
    stn = models.IntegerField()
    sdate = models.CharField(max_length=100)
    RRR = models.FloatField()
    Tmax = models.FloatField()
    T2 = models.FloatField()
    soil_temp_mean = models.FloatField()
    RH = models.FloatField()
    AH = models.FloatField()
    ff = models.FloatField()
    dirn = models.CharField(max_length=100)
    dp = models.FloatField()
