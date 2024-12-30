from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from subjects.models import Subject
from teachers.models import Teacher
from students.models import Student


def home(request):
    ctx = {'subjects_count': Subject.objects.count(),
           'teachers_count': Teacher.objects.count(),
           'students_count': Student.objects.count(),
           'groups_count': Group.objects.count(), }
    return render(request,'index.html', ctx)


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups }
    return render(request, 'groups/groups-list.html', ctx)

def group_add(request):
    class_teachers = Teacher.objects.all()
    students = Student.objects.all()
    group = None

    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        class_teacher_id = request.POST.get('class_teacher')

        if group_name and class_teacher_id:
            class_teacher = Teacher.objects.get(pk=class_teacher_id)
            Group.objects.create(
                group_name=group_name,
                class_teacher=class_teacher
            )
            return redirect('groups:list')

    return render(request, 'groups/group-form.html',
                  {'group': group, 'class_teachers': class_teachers, 'students': students, })


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'groups/group-detail.html', ctx)

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('groups:list')
    ctx = {'group' : group}
    return render(request, 'groups/group-delete-confirm.html', ctx)

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        class_teacher_id = request.POST.get('class_teacher')
        student_ids = request.POST.getlist('students')  # Tanlangan barcha o'quvchilarni oladi

        if group_name and class_teacher_id:
            group.group_name = group_name
            group.class_teacher_id = class_teacher_id
            group.save()


            selected_students = Student.objects.filter(pk__in=student_ids)
            group.students.set(selected_students)  # ManyToManyField uchun set() metodidan foydalanamiz

        return redirect(group.get_detail_url())


    context = {
        'group': group,
        'class_teachers': Teacher.objects.all(),
        'students': Student.objects.all(),
    }
    return render(request, 'groups/group-form.html', context)