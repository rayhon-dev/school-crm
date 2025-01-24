from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'display_teachers')
    search_fields = ['subject_name',]

    def display_teachers(self, obj):
        return ", ".join([f"{teacher.first_name} {teacher.last_name}" for teacher in obj.teachers.all()])
    display_teachers.short_description = 'Teachers'

admin.site.register(Subject, SubjectAdmin)
