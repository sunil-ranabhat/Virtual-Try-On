from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from myapp import *
import os
from django.core.files.storage import FileSystemStorage
from .main import main


# Create your views here.
def home_view(request):
    # Your logic for the home view
    return render(request, 'home.html') 

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrec!!!")
    return render(request, 'login.html')




def register_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same !!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return  redirect('login')
      
        
        
    return render(request, 'register.html') 



def logout_view(request):
    logout(request)
    return redirect('home') 

def upload_image(request):
    if request.method == 'POST':
        image_file = request.FILES['cloth-image']  # Correctly retrieve the uploaded file
        print(image_file)
        save_path = os.path.join('myapp/static', 'origin_web.jpg')
        
        # Open the file in write-binary mode and save the uploaded file to it
        with open(save_path, 'wb') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        return HttpResponse('Image uploaded successfully!')

    return render(request, 'imageUpload.html')

def upload_cloth(request):
    if request.method == 'POST':
        image_file = request.FILES['cloth-image']  # Correctly retrieve the uploaded file
        print(image_file)
        save_path = os.path.join('myapp/static', 'cloth_web.jpg')
        
        # Open the file in write-binary mode and save the uploaded file to it
        with open(save_path, 'wb') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        return HttpResponse('Image uploaded successfully!')

    return render(request, 'clothUpload.html')
    # if request.method == 'POST':
    #     f = request.files['file']
    #     f_src = 'static/cloth_web.jpg'
        
    #     f.save(f_src)
    #     return render(request, 'clothUpload.html')
    # return render(request, 'clothUpload.html')
def tryon_view(request):
    # if request.method== 'POST':
    # path= r'C:\Users\Sishir512\Desktop\Major project\virtual\myapp\main.py'
    # if os.path.exists(path):
    #     # Execute the script
    #     os.system("python " + path)
    # terminal_command ="python main.py"
    # os.system(terminal_command)
    main()
    return HttpResponse('Complete!')
