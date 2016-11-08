from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Tasks
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
	
	return render(request,'acelibraryapp/index.html',{'user': request.user,'user': request.user})
	






@login_required
def home(request):

	return render(request,'acelibraryapp/home.html',{})




def member_login(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('acelibraryapp.views.home')
			else:
				print("Disabled account")
		else:
			print("Invalid login")

	return render(request, 'acelibraryapp/index.html', {})

