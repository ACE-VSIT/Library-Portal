from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.

def home_page(request):
	return render(request, 'acelibraryapp/home_page.html', {})


@login_required
def Tasks(request):

	return render(request,'acelibraryapp/tasks.html',{})


def member_login(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('acelibraryapp.views.Tasks')
			else:
				print("Disabled account")
		else:
			print("Invalid login")

	return render(request, 'acelibraryapp/login.html', {})