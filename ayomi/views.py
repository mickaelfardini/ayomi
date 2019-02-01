from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf.urls import url
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def home(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			new_email = request.POST.get('email')
			firstname = request.POST.get('firstname')
			lastname = request.POST.get('lastname')
			if new_email:
				User.objects.filter(email=request.user.email).update(
					email=new_email, 
					username=new_email,
					first_name=firstname,
					last_name=lastname)
				return JsonResponse({
					'type': 'success', 
					'email': new_email,
					'firstname': firstname,
					'lastname': lastname
					})
			return JsonResponse({'type': 'error'})

		return render(request, 'home.html')
	else:
		return redirect('register')


def register(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		if not email or not password:
			return render(request, 'register.html', {'errors': 'Les champs doivent etre rempli'})

		user = User.objects.create_user(username=email, email=email, password=password)

		user = authenticate(username=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
	return render(request, 'register.html')