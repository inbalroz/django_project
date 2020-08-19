from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.TextField(max_length=9, primary_key=True)
    content = models.TextField(max_length=550, default='0'*550)
    log = models.TextField(max_length=1500)

    def __str__(self):
        return "{} , {}, {}".format(str(self.id), self.content, self.log)

