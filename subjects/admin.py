from django.contrib import admin
from .models import Subject
from teachers.models import Teacher


class TeacherInline(admin.StackedInline):
    model = Teacher
    extra = 1


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'display_teachers')
    search_fields = ['subject_name',]
    inlines = [TeacherInline]

    def display_teachers(self, obj):
        return ", ".join([f"{teacher.first_name} {teacher.last_name}" for teacher in obj.teachers.all()])
    display_teachers.short_description = 'Teachers'

admin.site.register(Subject, SubjectAdmin)




