from django.shortcuts import render
from .forms import studentRegisteration
from .models import User
from django.http import JsonResponse
# Create your views here.

def home(request):
    form= studentRegisteration()
    stud= User.objects.all()
    return render(request, 'enroll/home.html', {'form':form, 'stu':stud})

def save_data(request):
    if request.method=='POST':
        form= studentRegisteration(request.POST)
        if form.is_valid():
            sid= request.POST.get('stuid')
            name= request.POST['name']
            email= request.POST['email']
            password= request.POST['password']
            if (sid==''): # if sid is empty, means we are creating a new student 
                usr= User(name=name, email=email, password=password)
            else:
                usr= User(id=sid, name=name, email=email, password=password)
            usr.save()

            stud= User.objects.values() # will give all the data like name, email & password 
            # print(stud)
            student_data= list(stud)

            return JsonResponse({'status':'Save', 'student_data':student_data})
        
        else:
            return JsonResponse({'status':0})

def delete_data(request):
    if request.method=='POST':
        id= request.POST.get('sid')
        pi= User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    
    else:
        return JsonResponse({'status':0})
    

def edit_data(request):
    if request.method=='POST':
        id= request.POST.get('sid')
        student= User.objects.get(pk=id)
        student_data= {'id':student.id, 'name':student.name, 'email':student.email, 'password':student.password}
        return JsonResponse(student_data)
    
    else:
        return JsonResponse({'status':0})