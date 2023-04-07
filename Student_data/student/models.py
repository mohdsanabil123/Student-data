from django.db import models

# Create your models here.

class Student( models.Model ):
    s_id = models.IntegerField()
    s_name = models.CharField( max_length=50 )
    s_age = models.IntegerField()
    s_email = models.EmailField()
    s_contact = models.CharField( max_length=20 )
    
    def __str__(self):
        return self.s_name