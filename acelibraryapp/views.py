from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Tasks
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from django.template.context import RequestContext


# Create your views here.


def facebook_login(request):

	#context = RequestContext(request,{'request': request,'user': request.user})

	return render(request,'acelibraryapp/fblogin.html',{'request': request,'user': request.user})


@login_required
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

@login_required
def showTasks(request):

	tasks = Tasks.objects.filter(approval_status=True)

	return render(request, 'acelibraryapp/tasks.html',{'tasks':tasks})


@login_required
def getTasks(request, task):

	if request.method =="POST":
		#run query to insert task as a new row in Task Table
		# save and commit the changes
		return task

@login_required
def member_logout(request):
	logout(request)
	# Take the user back to the homepage.
	return HttpResponseRedirect('acelibraryapp/index.html')


	





'''
@login_required
def getAttendance(request):

	if request.method == "POST":
		#Srijit kese dega ?


@login_required
def getResource(request):

	if request.method=="POST":
		# run query to insert new resource from user


@login_required
def showResources(request):
	
	if request.method=="POST":
		#execute query to return all resources which are approved by admin


@login_required
def showAttendane(request):

	# execute query to return attendance of "authenticated user" 




def getSolution(request, solution):

	#execute query to insert solution by authenticated user

'''