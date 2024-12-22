from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from app_login.forms import SignupForm
# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form': form, 'registered': registered}
    return render(request, 'applogin/signup.html', dict)



def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('app_blog:blog_list'))
    return render(request, 'applogin/login.html', {'form': form})


@login_required(login_url='app_login:login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_blog:blog_list'))
