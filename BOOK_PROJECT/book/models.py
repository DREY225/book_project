from django.db import models

# Create your models here.

class Book(models.Model):
    
    book_type = [
        ('RM','Roman'),
        ('NV','Nouvelle'),
        ('PT','Pièce de théatre'),
        ('PS','Poésie')
    ]

    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    book_gender = models.CharField(max_length=2, choices = book_type)
    
    
    class Meta:
        db_table = 'livres'
        managed = True
        verbose_name = 'livre'
        verbose_name_plural = 'livres'