from django.db import models
from django.conf import settings
import datetime

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='', blank=True)
    phone = models.CharField('phone', max_length=16)
    birthday = models.DateField("birthday", default=datetime.date.today)
    gender = models.CharField('gender', max_length=50)
    org = models.CharField('org', max_length=64)
    job = models.CharField('job', max_length=64)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)