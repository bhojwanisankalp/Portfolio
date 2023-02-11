from django.core.management.base import BaseCommand
from userapp.models import User, ActivityPeriod
import pprint
import json
from datetime import datetime


class Command(BaseCommand):
    """ 
        Custom Command Manager To Populate Users for provided JSON File
        Required Json String Sample:
        [{
            "id": "W012A3CDE",
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activity_periods": [{
                    "start_time": "Feb 1 2020  1:33PM",
                    "end_time": "Feb 1 2020 1:54PM"
                },
                {
                    "start_time": "Mar 1 2020  11:11AM",
                    "end_time": "Mar 1 2020 2:00PM"
                },
                {
                    "start_time": "Mar 16 2020  5:33PM",
                    "end_time": "Mar 16 2020 8:02PM"
                }
            ]
        }]
    """
    help = 'Populate Users with ActivityPeriods'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        with open(options['path'], 'r') as stream:
            users = json.load(stream)
            for user in users:
                user_instance, _ = User.objects.get_or_create(pk=user['id'])
                user_instance.real_name = user['real_name']
                user_instance.tz = user['tz']
                user_instance.save()
                try:
                    user_instance.save()
                    for activity in user['activity_periods']:
                        start_time = datetime.strptime(activity['start_time'], '%b %d %Y %I:%M%p')
                        end_time = datetime.strptime(activity['end_time'], '%b %d %Y %I:%M%p')
                        activity_instance = ActivityPeriod.objects.create(end_time = end_time,
                                                                          start_time = start_time,
                                                                          user = user_instance)
                except Exception as e:
                    print(e)
            self.stdout.write(self.style.SUCCESS('Successfully created users'))
        