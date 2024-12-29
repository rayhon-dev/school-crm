from django.db import models
from subjects.models import Subject
from django.shortcuts import reverse

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='teachers')
    phone = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    experience = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='teachers_photos/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    def get_detail_url(self):
        return reverse('teachers:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('teachers:update', args=[self.pk])
