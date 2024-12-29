from django.shortcuts import render, redirect, get_object_or_404
from subjects.models import Subject
from .models import Teacher



def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers }
    return render(request, 'teachers/teachers-list.html', ctx)

def teacher_add(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_id = request.POST.get('subject')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        photo = request.FILES.get('photo')

        if first_name and last_name and subject_id and phone and email and experience and photo:
            subject = Subject.objects.get(pk=subject_id)
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subject=subject,
                phone=phone,
                email=email,
                experience=experience,
                photo=photo
            )
            return redirect('teachers:list')
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return  render(request, 'teachers/teacher-form.html', ctx)

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    ctx = {'teacher': teacher}
    return render(request, 'teachers/teacher-detail.html', ctx)

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers:list')
    ctx = {'teacher' : teacher}
    return render(request, 'teachers/teacher-delete-confirm.html', ctx)

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_id = request.POST.get('subject')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        photo = request.FILES.get('photo')

        if first_name and last_name and subject_id and phone and email and experience and photo:
            subject = Subject.objects.get(pk=subject_id)
            teacher.first_name = first_name
            teacher.last_name = last_name
            teacher.subject = subject
            teacher.phone = phone
            teacher.email = email
            teacher.experience = experience
            teacher.photo = photo

        teacher.save()

        return redirect(teacher.get_detail_url())

    ctx = {'teacher': teacher }
    return render(request, 'teachers/teacher-form.html', ctx)

