from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordChangingForm

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		username = username +'@astanait.edu.kz'
		request.session['person'] = {'barcode' : username}
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request,("There was an error loggin in, Try again...!"))
			return redirect('login')	
	else:	
		return render(request,'authenticate/login.html',{})


def logout_user(request):
	logout(request)
	messages.success(request,("You Were Logged out!"))
	return redirect('login')

def settings(request):
    if request.method == 'POST':
        form = PasswordChangingForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangingForm(request.user)
    return render(request, 'authenticate/settings.html', {
        'form': form
    })

