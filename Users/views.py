from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserLogin, UserRegistration

def user_signUp(request):
	form = UserRegistration(request.POST or None)
	if form.is_valid():
		password = form.cleaned_data.get("password")
		instance = form.save(commit=False)
		# encrypting the password
		instance.set_password(password)
		# saving after encrypting the password
		instance.save()
		return redirect("login")

	context = {
				"title": "Sign Up",
				"form": form,
			  }
	return render(request, "signUp.html", context)

def user_login(request):
	form = UserLogin(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")

		user = authenticate(request, username=username,
									 password=password)
		print(user)
		if user:
			login(request, user)
			return redirect("Journals:all")

	context = {
				"title": "Login",
				"form": form
			  }
	return render(request, "login.html", context)

def user_logout(request):
	logout(request)
	return redirect("login")