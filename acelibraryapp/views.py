from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import View
import json

# Create your views here.

class TaskView(View):

	def get_tasks():  
		pass

	def get(self, request):
		#process request 
		return render(request,'acelibraryapp/tasks.html',{})

class Authentication(View):


	def __init__(self):
		
		self.name = ''
		self.email = ''
		self.uid = ''		

	import json
	''' Test if user is authorized to access library resources '''
	def isMember(self,name):
		#print (name)
		
		with open('acelibraryapp/ace_membors.json') as json_data:
			data = json.load(json_data)

		if name in [name['name'] for name in data]:
			return True
		return False

	def get(self, request):

		if request.user.is_active and self.isMember(str(request.user.first_name) + " " + str(request.user.last_name)):
			return redirect('/home')
		else :
			auth_logout(request)

		return render(request,'acelibraryapp/index.html',{'user': request.user,'user': request.user})


class HomePage(Authentication):

	def get(self, request):

		if not self.isMember(str(request.user.first_name) + " " + str(request.user.last_name)):
			auth_logout(request)
			return redirect('/')

		return render(request, 'acelibraryapp/home.html')

'''
@login_required(login_url='/')
def home(request):


	return render(request, 'acelibraryapp/home.html')
'''
'''
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

'''