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
from .models import Tasks, Resources, Categories

# Create your views here.

class Authentication(View):
	
	data = {}
	
	''' Test if user is authorized to access library resources '''
	def isMember(self,name):	
		
		with open('acelibraryapp/ace_membors.json') as json_data:
			data = json.load(json_data)
		data = (item for item in data if item["name"] == name).__next__()
		if (data['valid'] ==3 or data['valid']==4) and name == data['name']:
			return True
		return False

	def fetchDetails(self,name):

		with open('acelibraryapp/ace_membors.json') as json_data:
			data = json.load(json_data)
		data = (item for item in data if item["name"] == name).__next__()
		if data['valid']==3: data['valid']='Core Member'
		if data['valid']==4: data['valid']='Member'
		return data

	def get(self, request):
		#name = str(request.user.first_name) + " " + str(request.user.last_name) #throws exception 
		if request.user.is_active and self.isMember(str(request.user.first_name) + " " + str(request.user.last_name)):
			Authentication.data = self.fetchDetails(str(request.user.first_name) + " " + str(request.user.last_name)) 			
			return redirect('/home')
		else :
			auth_logout(request)
		return render(request,'acelibraryapp/index.html',{'user': request.user})


class HomePage(Authentication):
	
	def __init__(self):
		self.user = Authentication.data
		self.valid = self.user['valid']

	def get(self, request):

		name = str(request.user.first_name) + " " + str(request.user.last_name)
		#print Authentication.data
		if not self.isMember(name):
			auth_logout(request)
			return redirect('/')
		return render(request, 'acelibraryapp/home.html', {'valid':self.valid})


class ResourceView(Authentication):

	def __init__(self):
		
		self.user = Authentication.data
		self.valid = self.user['valid']

	def fetch_categories(self):
		categories = Categories.objects.all()
		return categories

	def get(self, request):

		categories = self.fetch_categories()

		return render(request,'acelibraryapp/resource.html',{'valid':self.valid, 'categories' : categories})


class TaskView(Authentication):

	def __init__(self):
			
		self.user = Authentication.data
		self.valid = self.user['valid']

	def fetch_tasks(self):  
		tasks = Tasks.objects.filter(approval_status=True)
		return tasks

	def get(self, request):
		
		tasks = self.fetch_tasks()
		
		return render(request,'acelibraryapp/tasks.html',{'valid':self.valid, 'tasks':tasks})



class ResourceDetails(ResourceView):

	def __init__(self):

		self.user = Authentication.data
		self.valid = self.user['valid']


	def fetch_resource(self,string):
		resource = get_object_or_404(Resources, couse_diff=string)
		return resource

	
	def get(self, request):

		return render(request, 'acelibraryapp/resource_detail.html',{'valid':self.valid})


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
'''
@login_required(login_url='/')
def python(request):

	name = str(request.user.first_name) + " " + str(request.user.last_name)
	auth = Authentication()

	return render(request,'acelibraryapp/python.html',Authentication.fetchDetails(auth,name))
'''


def resource_details(request, pk):
	
	category = get_object_or_404(Categories, pk=pk)
	resources = Resources.objects.filter(cat=category)	
	return render(request, 'acelibraryapp/resource_detail.html', {'resources': resources, 'category':category})

