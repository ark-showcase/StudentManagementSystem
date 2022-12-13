from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Address
from . import forms

# Create your views here.

def index(request):
    student_list = Student.objects.order_by('std_no')
    dict = {'title': "Students", 'student_list': student_list}
    return render(request, 'info/index.html' ,context = dict)

def address_list(request):
    address_list = Address.objects.order_by('city')
    dict = {'title': "Address", 'address_list': address_list}
    return render(request, 'info/address_list.html', context = dict)


def student_detail(request, student_id):
    student_info = Student.objects.get(id = student_id)
    student_address = Address.objects.filter(student_id = student_id)
    dict = {'title': "student_info", 'student_info': student_info, 'student_address': student_address}
    return render(request, 'info/student_detail.html', context=dict)

def address_detail(request, address_id):
    address_info = Address.objects.get(id = address_id)
    print("adress_id: "+str(address_info.student_id))
    address_student = Student.objects.get(id = address_info.student_id)
    dict = {'title': address_info, 'address_info': address_info, 'address_student': address_student}
    return render(request, 'info/address_detail.html', context=dict)

def student_form(request):
    form = forms.StudentForm()

    if request.method == 'POST':
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    dict = {'title': "Add Student", 'student_form':form}
    return render(request, 'info/student_form.html', context = dict)

def address_form(request):
    form = forms.AddressForm()

    if request.method == 'POST':
        form = forms.AddressForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    dict = {'title': "Add Address", 'address_form': form}
    return render(request, 'info/album_form.html', context = dict)

def update_student(request,id):
    student = Student.objects.get(pk=id)
    form = forms.StudentForm(instance=student)

    if request.method == 'POST':
        form = forms.StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save(commit=True)
            return student_detail(request, id)

    dict = {'title': "Update " + str(student), 'form': form}
    return render(request, 'info/update_student.html', context=dict)

def update_address(request,id):
    address = Address.objects.get(pk=id)
    form = forms.AddressForm(instance=address)

    if request.method == 'POST':
        form = forms.AddressForm(request.POST, instance=address)

        if form.is_valid():
            form.save(commit=True)
            return address_detail(request, id)

    dict = {'title': "Update " + str(address), 'form': form}
    return render(request, 'info/update_address.html', context=dict)

def delete_address(request,id):
    address = Address.objects.get(pk=id).delete()
    return address_list(request)



def delete_student(request,id):
    student = Student.objects.get(pk=id).delete()
    return index(request)