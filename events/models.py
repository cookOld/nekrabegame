from django.db import models
import datetime
from accounts.models import Profile

class Event(models.Model):
     title = models.CharField('Название', max_length=50)
     desc = models.TextField('Название')
     user_id = models.IntegerField('user_id')
     thumb = models.ImageField(upload_to='', blank=True)
     x = models.FloatField('y', blank=True)
     y = models.FloatField('y', blank=True)
     status = models.CharField('status', max_length=64)
     acesss = models.CharField('acess', max_length=64)
     date = models.DateField("date", default=datetime.date.today)
     start_time = models.TimeField(u"From", blank=True, null=True)
     end_time = models.TimeField(u"End", blank=True, null=True)
     event_type = models.CharField('event_type', max_length=64)
class E_request(models.Model):
     event = models.ForeignKey(Event, on_delete=models.CASCADE, unique=False)
     user = models.ForeignKey(Profile, on_delete=models.CASCADE, unique=False)
     permission = models.IntegerField('permission')