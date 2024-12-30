from django.db import models
from teachers.models import Teacher

class Group(models.Model):
    group_name = models.CharField(max_length=100)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, related_name='group')
    students = models.ManyToManyField('students.Student', related_name='group_list')  # String ishlatildi

    def __str__(self):
        return self.group_name

    def get_detail_url(self):
        from django.shortcuts import reverse
        return reverse('groups:detail', args=[self.pk])

    def get_delete_url(self):
        from django.shortcuts import reverse
        return reverse('groups:delete', args=[self.pk])

    def get_update_url(self):
        from django.shortcuts import reverse
        return reverse('groups:update', args=[self.pk])
