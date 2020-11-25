from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField('Tipo de usuario', max_length=50)

    class Meta:
        verbose_name = 'User type'
        verbose_name_plural = 'User types'
        ordering = ['id']

    def __str__(self):
        return self.name
