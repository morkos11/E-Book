from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.admin.forms import AuthenticationForm, PasswordChangeForm
from .forms import SignupForm, StudentForm, AdminForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

def complete_signup(request):
    return render(request, 'completeSignup.html')
def signup_form_Page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return reverse_lazy('accounts:signup_complete')
    else:
        form = SignupForm()
    context = {'form':form}
    return render(request, 'signup.html', context)

def student_signup(request):
    if request.method=='POST':
        form= StudentForm(request.POST, request.FILES)
        if form.is_valid():
           form.save(commit=False)
           form.instance.user = request.user
           if request.FILES:
              form.profile_pic = request.FILES['profile_pic']
           form.save()
           return redirect('/')
    else:
        form = StudentForm()
    context ={'form':form}
    return render(request, 'studentSignup.html', context)

def admin_signup(request):
    if request.method=='POST':
        form= AdminForm(request.POST, request.FILES)
        if form.is_valid():
           form.save(commit=False)
           form.instance.user = request.user
           if request.FILES:
              form.profile_pic = request.FILES['profile_pic']
           form.save()
           return redirect('/')
    else:
        form = AdminForm()
    context ={'form':form}
    return render(request, 'adminSignup.html', context)


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'logout.html')
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user = authenticate(username=username, password=password)
           login(request,user)
           return redirect('/')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'login.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password1']
            user = form.save()
            update_session_auth_hash(request, user)
            user_auth = authenticate(username=request.user.username,password=new_password)
            login(request,user_auth)
            messages.success(request,'Password had seccessfully changed ')
        else:
            messages.error(request,'An error happened and password had not change')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request,'reset_password/change_password.html',context)



