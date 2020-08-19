from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from string import Template


class UserRegisterForm(UserCreationForm):
    #state = forms.Textarea
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['academic_position', 'article_reviewed']
        labels = {'academic_position' : 'Academic position', 'article_reviewed': 'Experience in paper reviews' }
        widgets = {'academic_position' : forms.Select(choices=[('none','None'),('undergraduate','Undergraduate'),('graduate student','Graduate student'),('faculty','Faculty')]),
                   'article_reviewed' : forms.Select(choices=[('1','I have substantial experience in bidding on papers in academic conferences (via EasyChair, ConfMaster, etc.)'),
                                                              ('2',' I have some experience in bidding on papers in academic conferences (via EasyChair, ConfMaster, etc.)'),
                                                              ('3',' I have experience in reviewing academic papers, but did not participate in paper bidding.'),
                                                              ('4','  I have no experience in  reviewing academic papers.')]) }

    check1 = forms.BooleanField(required = True, label="Every paper is worth a certain amount of bidding points. A high number means a higher chance to get the paper due to lower demand.")
    check2 = forms.BooleanField(required = True, label="You have to click 'save' before moving to another page or tab (including the Instructions tab).")