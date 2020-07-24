from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app import forms
from first_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date') # import models and make queries
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', date_dict) # inject 'em to the templates

@login_required
def user_logout(request): # use the decorator for the special page!
    logout(request) # automatically logged out with the method!
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid:
            user = user_form.save() # get data from input form
            user.set_password(user.password)
            user.save() # store the data in the DB

            profile = profile_form.save(commit=False)
            profile.user = user # one to one relationship between user and profile

            if 'profile_pic' in request.FILES: # load files from request directly, instead of saving the pictures on the file system
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username') # get POST data from templates with the name
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'first_app/login.html', {})

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    return render(request, 'first_app/relative_url_templates.html')

def form_name_view(request):
    # 1. make instance
    # 2. store it in context
    # 3. load form with {{ form.as_p }} on template
    form = forms.FormName() # make instance

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME:" + form.cleaned_data['name']) # grab the data
            print("EMAIL:" + form.cleaned_data['email'])
            print("TEXT:" + form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form': form})