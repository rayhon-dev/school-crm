from django.contrib import admin
from .models import Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'display_class_teacher', 'display_students')
    search_fields = ['group_name', 'class_teacher__first_name', 'class_teacher__last_name',
                     'students__full_name']

    def display_class_teacher(self, obj):
        return f"{obj.class_teacher.first_name} {obj.class_teacher.last_name}"
    display_class_teacher.short_description = 'Class Teacher'

    def display_students(self, obj):
        return ", ".join(student.full_name for student in obj.students.all())

    display_students.short_description = 'Students'

admin.site.register(Group, GroupAdmin)
