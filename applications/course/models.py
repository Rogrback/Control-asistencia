from django.db import models
from applications.teacher.models import Teacher

class Course(models.Model):
    name = models.CharField('Nombre del curso', max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['id']

    def __str__(self):
        return self.name