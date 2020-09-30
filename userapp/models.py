from django.db import models
import uuid
import pytz
from .utils import get_pk

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

class User(models.Model):
	""" Custom User Model """
	id = models.CharField(max_length=9, primary_key=True, default=get_pk)
	real_name = models.CharField(max_length=50, null=False, default='')
	tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
	created_at  = models.DateTimeField(auto_now_add = True, null = True)
	updated_at = models.DateTimeField(auto_now = True, null = True)

	def __str__(self):
		return self.real_name

	def get_activity_periods(self):
		""" To get associated ActivityPeriod model instance. """
		return ActivityPeriod.objects.filter(user = self)

class ActivityPeriod(models.Model):
	""" User Activites Model """
	user = models.ForeignKey(User ,on_delete=models.CASCADE, null = True)
	start_time = models.DateTimeField(null = True)
	end_time = models.DateTimeField(null = True)

	def __str__(self):
		return self.user.real_name + ' Date ' + self.start_time.strftime("%d-%m-%y")
