from django.db import models

# Create your models here.
class Author(models.Model):
    
    country_list = [
        ('CI','Ivory Coast'),
        ('SN','Senegal'),
        ('ML','Mali'),
        ('TG','Togo'),
        ('BF','Burkina Faso')
    ]

    name = models.CharField(max_length = 100)
    phome = models.CharField(max_length = 15)
    email = models.CharField(max_length = 30)
    country = models.CharField(max_length=2, choices=country_list)
    
    
    class Meta:
        db_table = 'auteurs'
        managed = True
        verbose_name = 'auteur'
        verbose_name_plural = 'auteurs'
    
    