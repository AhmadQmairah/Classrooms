from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import Classroom,Student
from .forms import ClassroomForm,SignUpForm,LogInForm,StudentForm

def classroom_list(request):
    classrooms = Classroom.objects.all()
    context = {
        "classrooms": classrooms,
    }
    return render(request, 'classroom_list.html', context)


def classroom_detail(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    context = {
        "classroom": classroom,
        "students" : (Student.objects.filter(classroom=classroom)).order_by("-exam_grade","-name")
    }
    return render(request, 'classroom_detail.html', context)


def classroom_create(request):
    if(request.user.is_anonymous):
        messages.success(request, "LogIn Please")
        return redirect('LogIn')

    form = ClassroomForm()
    if request.method == "POST":
        form = ClassroomForm(request.POST, request.FILES or None)
        if form.is_valid():
            teacher=form.save(commit=False)
            teacher.Teacher=request.user
            teacher.save()
            messages.success(request, "Successfully Created!")
            return redirect('classroom-list')
        print (form.errors)
    context = {
    "form": form,
    }
    return render(request, 'create_classroom.html', context)


def classroom_update(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    form = ClassroomForm(instance=classroom)
    if request.method == "POST":
        form = ClassroomForm(request.POST, request.FILES or None, instance=classroom)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Edited!")
            return redirect('classroom-list')
        print (form.errors)
    context = {
    "form": form,
    "classroom": classroom,
    }
    return render(request, 'update_classroom.html', context)


def classroom_delete(request, classroom_id):
    Classroom.objects.get(id=classroom_id).delete()
    messages.success(request, "Successfully Deleted!")
    return redirect('classroom-list')


def SignUp(request):
    FORM=SignUpForm()

    if request.method=="POST":
        FORM=SignUpForm(request.POST)
        if FORM.is_valid():
            user =FORM.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('classroom-list')


    context={"form":FORM}
    return render(request,'SignUp.html',context)

def StudentADD(request,classroom_id):
    FORM=StudentForm()
    Class=Classroom.objects.get(id=classroom_id)
    if request.user != Class.Teacher :
        return redirect('classroom-list')
    if request.method=="POST":
        FORM=StudentForm(request.POST)
        if FORM.is_valid():
            Class=FORM.save(commit=False)
            Class.classroom= Classroom.objects.get(id=classroom_id)
            Class.save()
            return redirect('classroom-list')


    context={"form":FORM}
    return render(request,'AddStudent.html',context)

def LogIn(request):
    FORM=LogInForm()

    if request.method=="POST":
        FORM=LogInForm(request.POST)
        if FORM.is_valid():
            username =FORM.cleaned_data["username"]
            password =FORM.cleaned_data["password"]
            user=authenticate(username=username,password=password)
            if(user):
                login(request,user=user)
                return redirect('classroom-list')
            else:
                return redirect('LogIn')


    context={"form":FORM}
    return render(request,'LogIn.html',context)
    
    
def LogOut(request):
    logout(request)
    return redirect('classroom-list')

def StudentUpdate(request,student_id):
    stud = Student.objects.get(id=student_id)
    form = StudentForm(instance=stud)
    if request.user != stud.classroom.Teacher :
        return redirect('classroom-list')

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES or None, instance=stud)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Edited!")
            return redirect('classroom-list')
        

    context = {
    "form": form,
    "student": stud,
    }
    return render(request, 'StudentUpdate.html', context)


def Studentdelete(request,student_id):
    stud = Student.objects.get(id=student_id)
    
    if request.user != stud.classroom.Teacher :
        return redirect('classroom-list')

    
    stud.delete()
    return redirect('classroom-list')
    