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
                   'article_reviewed' : forms.Select(choices=[('substantial experience','I have substantial experience in bidding on papers in academic conferences (via EasyChair, ConfMaster, etc.)'),
                                                              ('some experience',' I have some experience in bidding on papers in academic conferences (via EasyChair, ConfMaster, etc.)'),
                                                              ('experience but did not participate in paper bidding',' I have experience in reviewing academic papers, but did not participate in paper bidding.'),
                                                              ('no experience','  I have no experience in  reviewing academic papers.')]) }

    check1 = forms.BooleanField(required = True, label="Please sign the attached informed consent form below.")
    check2 = forms.BooleanField(required = True, label="You have to click 'save' before moving to another page or tab.")