from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'display_group',)
    search_fields = ['full_name', 'address']

    def display_group(self, obj):
        return obj.group.group_name
    display_group.short_description = 'Group'



admin.site.register(Student, StudentAdmin)
