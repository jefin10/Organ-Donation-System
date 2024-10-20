from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import DoctorLoginForm
from tables.models import Doctor
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request, 'signup.html')
def pledge(request):
    return render(request,'pledge.html')



from django.contrib import messages
from tables.models import LoginInfo
from django.contrib.auth.hashers import check_password

def doctor_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            login_user = LoginInfo.objects.get(username=username)
            
            if check_password(password, login_user.password):  
                return redirect('doctor_view') 
            else:
                messages.error(request, 'Invalid password')
        except LoginInfo.DoesNotExist:
            messages.error(request, 'Invalid username')

    form = DoctorLoginForm() 
    return render(request, 'login.html', {'form': form})
@login_required
def doctor_detail_view(request, doctor_id):
    doctor = Doctor.objects.get(doctor_id=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})
from django.contrib.auth import logout

def doctor_logout_view(request):
    logout(request)  
    return redirect('doctor_login')