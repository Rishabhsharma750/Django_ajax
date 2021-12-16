from django.db import models

class Data(models.Model):
    fname = models.CharField(max_length=255,null=True,blank=True)
    lname = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.fname
