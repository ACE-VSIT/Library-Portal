from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Problem


# Create your views here.

def index(request):
	return render(request, 'acelibraryapp/index.html', {})


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


def showTasks(request):

	tasks = Problem.objects.filter(approval_status=True)

	return render(request, 'acelibraryapp/tasks.html',{'tasks':tasks})




