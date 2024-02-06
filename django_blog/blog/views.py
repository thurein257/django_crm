from urllib import request
from django.shortcuts import render,redirect
from blog.models import Record
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Record


def record(request):
    if request.method =='GET':
        records = Record.objects.all()
    return render (request, 'record.html',{'records':records})

@login_required(login_url='/login')
def add_record(request):
    if request.method == "POST":
        add_record = Record.objects.create(
            name = request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            zipcode=request.POST.get('zipcode')
        )
        add_record.save()
        messages.success(request,"Record Added....")
        return redirect('/')
    return render (request, 'add_record.html',{})


def data_update(request, user_id):
    if request.method =='GET':
        data_update = Record.objects.get(id=user_id)
    return render (request, 'data_update.html',{'data_update':data_update})

@login_required(login_url='/login')
def edit(request, user_id):
    if request.user.is_authenticated:
        if request.method =='GET':
            data_update = Record.objects.get(id=user_id)
            return render (request, 'edit.html',{'data_update':data_update})


        if request.method =="POST":
            data_update = Record.objects.get(id=user_id)
            data_update.name = request.POST.get('name')
            data_update.email = request.POST.get('email')
            data_update.phone = request.POST.get('phone')
            data_update.address = request.POST.get('address')
            data_update.city = request.POST.get('city')

            data_update.save()
            messages.success(request,"User Data Has Been Updated Successfully....")
            return redirect('/')

@login_required(login_url='/login')
def delete(request, user_id):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=user_id)
        delete_record.delete()
        messages.success(request,"Record Deleted Successfully....")
        return redirect('/')
    else:
        messages.success(request,"You Must Be Logged In To Do That....")
        return redirect('/')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"User Login Successfully....")
            return redirect('/')
        else:
            messages.success(request,"There Was An Error Logging In, Please Create New Account From Register Link !")
    return render (request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = User.objects.create_user(username=username, password=password)
        my_user.save()
        messages.success(request,"Registration Successfully....")
        return redirect('/login')
    return render (request, 'register.html',{})

def logout(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out...")
    return render(request, 'login.html')

def handling_404(request, exception=None):
    return render(request, '404.html',status=404)