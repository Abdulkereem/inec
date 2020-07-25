from django.db import models

class Id_Card(models.Model):
    header = models.CharField(max_length=500,blank=True)
    logo = models.ImageField(upload_to="logo", blank=True)
    name = models.CharField(max_length=500,blank=True)
    passport = models.ImageField(upload_to="passport", blank=True)
    identity_text= models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.name
