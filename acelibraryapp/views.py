from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):

	if request.user.is_active:
		return redirect(home)

	return render(request,'acelibraryapp/index.html',{'user': request.user,'user': request.user})


@login_required(login_url='/')
def home(request):
	return render(request, 'acelibraryapp/home.html')


@login_required(login_url='/')
def tasks(request):

	# Insert query to get approved tasks

	return render(request,'acelibraryapp/tasks.html',{})

