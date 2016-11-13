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

class Authentication(View):

	def __init__(self):
		
		self.name = ''
		self.email = ''
		self.uid = ''
		self.valid = 4		

	''' Test if user is authorized to access library resources '''
	def isMember(self,name):	
		
		with open('acelibraryapp/ace_membors.json') as json_data:
			data = json.load(json_data)

		data = (item for item in data if item["name"] == name).next()
		if (data['valid'] ==3 or data['valid']==4) and name == data['name']:
			return True
		
		return False

	def fetchDetails(self,name):

		with open('acelibraryapp/ace_membors.json') as json_data:
			data = json.load(json_data)

		data = (item for item in data if item["name"] == name).next()
		if data['valid']==3: data['valid']='Core Member'
		if data['valid']==4: data['valid']='Member'
		return data

	def get(self, request):

		#name = str(request.user.first_name) + " " + str(request.user.last_name) #throws exception 
		if request.user.is_active and self.isMember(str(request.user.first_name) + " " + str(request.user.last_name)):
			return redirect('/home')
		else :
			auth_logout(request)
		return render(request,'acelibraryapp/index.html',{'user': request.user,'user': request.user})


class HomePage(Authentication):

	def __init__(self):
		self.name=''
	
	def get(self, request):

		name = str(request.user.first_name) + " " + str(request.user.last_name)

		if not self.isMember(name):
			auth_logout(request)
			return redirect('/')
			
		return render(request, 'acelibraryapp/home.html', self.fetchDetails(name))



class Resources(HomePage):

	def fetch_resouces():
		pass


	def get(self, request):

		name = str(request.user.first_name) + " " + str(request.user.last_name)

		return render(request,'acelibraryapp/resource.html',self.fetchDetails(name))




'''
@login_required(login_url='/')
def resource(request):

	# Insert query to get approved resource
	name = str(request.user.first_name) + " " + str(request.user.last_name)
	auth = Authentication()

	return render(request,'acelibraryapp/resource.html',Authentication.fetchDetails(auth,name))

'''


@login_required(login_url='/')
def python(request):

	name = str(request.user.first_name) + " " + str(request.user.last_name)
	auth = Authentication()

	return render(request,'acelibraryapp/python.html',Authentication.fetchDetails(auth,name))


class TaskView(HomePage):

	def get_tasks():  
		pass

	def get(self, request):
		
		name = str(request.user.first_name) + " " + str(request.user.last_name)

		return render(request,'acelibraryapp/tasks.html',self.fetchDetails(name))

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