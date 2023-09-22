from django.db import models

# Create your models here.
class Author(models.Model):
    
    country_list = [
        ('CIV','Ivory Coast'),
        ('SN','Senegal'),
        ('ML','Mali'),
        ('TG','Togo'),
        ('BF','Burkina Faso')
    ]
    
    
    name = models.CharField(max_length = 100)
    phome = models.CharField(max_length = 15)
    email = models.CharField(max_length = 30)
    country = models.Choices(country_list)
    
    