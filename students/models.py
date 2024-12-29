from django.db import models
from groups.models import Group
from django.shortcuts import reverse


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    dob = models.DateField() # date_of_birth = dob
    phone = models.CharField(max_length=100)
    address = models.TextField()
    photo = models.ImageField(upload_to='students_photos/')

    def __str__(self):
        return self.full_name


    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])
