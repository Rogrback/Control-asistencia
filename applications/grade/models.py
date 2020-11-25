from django.db import models

class Grade(models.Model):
    name = models.CharField('Nombre del grado', max_length=50)

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'
        ordering = ['id']

    def __str__(self):
        return self.name