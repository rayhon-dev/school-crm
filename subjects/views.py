from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from teachers.models import Teacher
from django.views import View


def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects }
    return render(request, 'subjects/subjects-list.html', ctx)

def subject_add(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')

        if subject_name:
            Subject.objects.create(
                subject_name=subject_name,
            )
            return redirect('subjects:list')
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return  render(request, 'subjects/subject-form.html', ctx)

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    ctx = {'subject': subject}
    return render(request, 'subjects/subject-detail.html', ctx)

def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subjects:list')
    ctx = {'subject' : subject}
    return render(request, 'subjects/subject-delete-confirm.html', ctx)

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        teacher_ids = request.POST.getlist('teachers')


        if subject_name:
            subject.subject_name = subject_name
            subject.teachers.set(teacher_ids)  # O'qituvchilarni yangilash
            subject.save()
            return redirect(subject.get_detail_url())

    teachers = Teacher.objects.all()
    ctx = {'subject': subject, 'teachers': teachers}
    return render(request, 'subjects/subject-form.html', ctx)

