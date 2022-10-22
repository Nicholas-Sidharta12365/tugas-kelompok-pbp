from django.shortcuts import render
from childcare.models import Childcare
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='login/')
def show_childcare(request):

    user_log = request.user

    database = Childcare.objects.all().filter(user = user_log)

    context = {
        'data': database,
    }

    return render(request, 'childcare.html', context)

def show_json(request):

    data = Childcare.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("childcare:show_childcare")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('childcare:show_childcare'))
    response.delete_cookie('last_login')
    return 

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('/childcare/login/')
    
    context = {'form':form}
    return render(request, 'register.html', context)