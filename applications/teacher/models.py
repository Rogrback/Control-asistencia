from django.db import models
from applications.user_type.models import UserType

class Teacher(models.Model):
    id_card = models.CharField('DNI', max_length=8, primary_key=True)
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    phone = models.CharField('Telefono', max_length=9)
    user = models.CharField('Usuario', max_length=50)
    password = models.CharField('Contraseña', max_length=50)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['last_name']
        unique_together = ('id_card', 'first_name', 'last_name', 'phone', 'user', 'password', 'user_type')

    def __str__(self):
        return self.first_name + ' ' + self.last_name