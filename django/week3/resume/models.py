from django.db import models

# Create your models here.
def Education(models.Model):
	degre = models.TextField()
    locatoin = models.TextField()
    major = models.TextField()
    instatutoin = models.TextField()
    gpa = models.FloatField()

def Experiance(models.Model):
	Locatoin = models.TextField()
    description = models.TextField()
    tital = models.TextField()
    Start_date = models.DateField()
    End_date = models.DateField()