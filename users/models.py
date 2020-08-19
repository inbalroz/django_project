from django.db import models
from django.contrib.auth.models import User
import json
import os.path


with open(os.path.dirname(__file__) + '/../parameters.json') as f:
    data = json.load(f)




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    state = models.TextField(max_length=550, default='0'*550)
    log = models.TextField(max_length=1500, default=' ')
    group = models.CharField(max_length=1, default=' ')
    keywords = models.TextField(max_length=300, default=' ')
    prices = models.TextField(max_length=2500, default=' ')
    budget = models.CharField(max_length=8, default=data['budget'])
    academic_position = models.CharField(max_length=200, default=' ')
    article_reviewed = models.CharField(max_length=200, default=' ')
                                         


    def __str__(self):
        return "{}, {}".format(self.group, self.user.username)

    def keywords_as_list(self):
        return self.keywords.split(",")