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
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 35)
    country = models.CharField(max_length=2, choices=country_list)
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'auteurs'
        managed = True
        verbose_name = 'auteur'
        verbose_name_plural = 'auteurs'
    
    