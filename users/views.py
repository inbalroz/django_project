from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import UserRegisterForm, ProfileRegisterForm
from users.models import Profile
import random
import json
import os.path
from django.views.generic import View




with open(os.path.dirname(__file__) + '/../parameters.json') as f:
    json = json.load(f)

words = json["keywords"]

def registerA(request):
    messages = []
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            academic_position = profile_form.cleaned_data.get('academic_position')
            article_reviewed = profile_form.cleaned_data.get('article_reviewed')
            keywords = str(random.sample(words, json["keywords_num"]))
            keywords = keywords.replace("'","").replace("]","").replace("[","")
            range_a, range_b = json['range']
            prices = random.choices(range(range_a,range_b), k=550)
            for i,val in enumerate(prices):
                if val>json["max"]:
                    prices[i] = json["max"]
                elif val<json["min"]:
                    prices[i]= json["min"]
            prices = str(prices).replace("]","").replace("[","")
            profile = Profile(user=user, group='A', keywords=keywords, prices=prices, academic_position=academic_position, article_reviewed=article_reviewed)
            profile.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog-instructions')
        else:
            for error in form.errors.values():
                messages.append(error[0])       

    else:
        form = UserRegisterForm()
        profile_form = ProfileRegisterForm()
    
    context = {'form': form, 'profile_form': profile_form, 'messages': messages}
    return render(request, 'users/registerA.html', context)




def registerB(request):
    messages = []
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            academic_position = profile_form.cleaned_data.get('academic_position')
            article_reviewed = profile_form.cleaned_data.get('article_reviewed')
            keywords = str(random.sample(words, json["keywords_num"])).replace("'", "").replace("]", "").replace("[", "")
            profile = Profile(user=user, group='B', keywords=keywords, academic_position=academic_position, article_reviewed=article_reviewed)
            profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog-Binstructions')
        else:
            for error in form.errors.values():
                messages.append(error[0])       

    else:
        form = UserRegisterForm()
        profile_form = ProfileRegisterForm()
    
    context = {'form': form, 'profile_form': profile_form, 'messages': messages}
    return render(request, 'users/registerB.html', context)


def hebrewform(request):
    return render(request, 'users/hebrewform.html')

def englishform(request):
    return render(request, 'users/englishform.html')

def confirmation(request):
    return render(request, 'users/confirmation.html')



