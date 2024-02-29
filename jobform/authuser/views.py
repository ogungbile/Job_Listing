from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from hr.models import Hr

# Create your views here.

def register_candidate(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 
        if password != cpassword:
            msg = "Password did't match"
            return render(request,'authuser/hrregister.html',{'msg':msg})
        if User.objects.filter(username=username).exists():
            msg = "User already Exists.."
            return render(request, 'authuser/candidateregister.html',{'msg': msg}) 
        user = User.objects.create_user(username=username, email=email, password=password)
        
        login(request, user) 
        return redirect('candidate_dashboard') 

    return render(request,'authuser/candidateregister.html')

def register_hr(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 
        if password != cpassword:
            msg = "Password did't match"
            return render(request,'authuser/hrregister.html',{'msg':msg})
        if User.objects.filter(username=username).exists():
            msg = "User already Exists.."
            return render(request, 'authuser/candidateregister.html',{'msg': msg}) 
        user = User.objects.create_user(username=username, email=email, password=password)
        Hr(user=user).save()
        login(request, user) 
        return redirect('candidate_dashboard') 

    return render(request,'authuser/hrregister.html')

def login_user(request):
    msg = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if Hr.objects.filter(user=user).exists():
                return redirect('candidate_dashboard')
            else:
                return redirect('candidate_dashboard')
        else:
            msg = "InValid Username or Password"
    return render(request,'authuser/login.html',{'msg':msg})

def logoutUser(request):
    logout(request)
    return redirect('login_user')