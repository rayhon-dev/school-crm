from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from groups.models import Group



def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students }
    return render(request, 'students/students-list.html', ctx)

def student_add(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        group_id = request.POST.get('group')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')

        if full_name and group_id and dob and phone and address and photo:
            group = Group.objects.get(pk=group_id)
            Student.objects.create(
                full_name=full_name,
                group=group,
                dob=dob,
                phone=phone,
                address=address,
                photo=photo
            )
            return redirect('students:list')
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return  render(request, 'students/student-form.html', ctx)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request, 'students/student-detail.html', ctx)

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students:list')
    ctx = {'student' : student}
    return render(request, 'students/student-delete-confirm.html', ctx)

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    groups = Group.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        group_id = request.POST.get('group')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')

        if full_name and group_id and dob and phone and address:
            group = Group.objects.get(pk=group_id)
            student.full_name = full_name
            student.group = group
            student.dob = dob
            student.phone = phone
            student.address = address
            if photo:
                student.photo = photo
            student.save()

            return redirect(student.get_detail_url())

    ctx = {'student': student,
           'groups': groups }
    return render(request, 'students/student-form.html', ctx)

