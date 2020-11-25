from django.db import models
from applications.student.models import Student
from applications.course.models import Course
from datetime import date

STATE_CHOICES = [
    ('0', 'No asiste'),
    ('1', 'Asiste')
]

class Assistance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    state = models.CharField('Estado', max_length=20, choices=STATE_CHOICES)

    class Meta:
        verbose_name = 'Assistance'
        verbose_name_plural = 'Assistances'
        ordering = ['student']
        #unique_together = ('student', 'course', 'date', 'state')

    def __str__(self):
        return str(self.id) + ' ' + str(self.student) + ' ' + str(self.course) + ' ' + str(self.date) + ' ' + str(self.state)