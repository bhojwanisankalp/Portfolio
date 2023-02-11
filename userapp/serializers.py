from rest_framework import serializers
from .models import User, ActivityPeriod, Contact

class ActivityPeriodListSerializers(serializers.ModelSerializer):
	""" Serializers To serialize List of ActivityPeriod Model with associated User Model """

	#Change date time format according to required response
	start_time =  serializers.DateTimeField(format="%b %d %Y %I:%M%p")
	end_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p")

	class Meta:
		model = ActivityPeriod
		fields = ('start_time', 'end_time')

class UserSerializer(serializers.ModelSerializer):
	""" Serializers To serialize User Model """

	#Get associated ActivityPeriod Model serialized data
	activity_periods = ActivityPeriodListSerializers(source= "get_activity_periods", read_only=True, many=True)
	
	class Meta:
		model = User
		fields = ('id', 'real_name', 'tz', 'activity_periods')

class ContactSerializer(serializers.ModelSerializer):
	""" Serializers To serialize Contact Model """

	class Meta:
		model = Contact
		fields = ('name', 'email', 'description')