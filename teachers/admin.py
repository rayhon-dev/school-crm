from django.contrib import admin
from .models import Teacher
from groups.models import Group


class GroupInline(admin.StackedInline):
    model = Group
    extra = 1


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'display_subject', 'phone', 'email', 'experience', 'photo')
    search_fields = ['first_name', 'last_name', 'email', 'subject__subject_name']
    inlines = [GroupInline]



    def display_subject(self, obj):
        return obj.subject.subject_name

    display_subject.short_description = 'Subject'


admin.site.register(Teacher, TeacherAdmin)
