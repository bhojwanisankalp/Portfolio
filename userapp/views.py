from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from userapp.serializers import UserSerializer
from userapp.models import User
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users(request):
	"""
		API to get List of User Model
		sample output :
		{
		    "ok": true,
		    "members": [{
		            "id": "W07QCRPA4",
		            "real_name": "Glinda Southgood",
		            "tz": "Asia/Kolkata",
		            "activity_periods": [
		                {
		                    "start_time": "Feb 01 2020 01:33PM",
		                    "end_time": "Feb 01 2020 01:54PM"
		                },
		                {
		                    "start_time": "Mar 01 2020 11:11AM",
		                    "end_time": "Mar 01 2020 02:00PM"
		                },
		                {
		                    "start_time": "Mar 16 2020 05:33PM",
		                    "end_time": "Mar 16 2020 08:02PM"
		                }
		            ]
		        }
		    ]
		} 	
	"""
	try:
		users = User.objects.all()
		serializer = UserSerializer(users, many = True)
		context = {'ok':True, 'members':serializer.data}
		return Response(context)
	except Exception as e:
		print(e)
	context = {'ok':False, 'error':'Something went wrong'}
	return Response(context)