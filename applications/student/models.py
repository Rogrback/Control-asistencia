from django.db import models
from applications.grade.models import Grade

class Student(models.Model):
    student_enrollment = models.CharField('Matrícula_estudiante', max_length=6, primary_key=True)
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    photography = models.ImageField('Foto', upload_to='students')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['last_name']
        unique_together = ('student_enrollment', 'first_name', 'last_name', 'grade')

    def __str__(self):
        return self.first_name + " " + self.last_name
