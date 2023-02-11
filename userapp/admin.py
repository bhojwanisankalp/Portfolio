from django.contrib import admin
from .models import User, ActivityPeriod, Contact

# Register your models here.

admin.site.register(User)
admin.site.register(ActivityPeriod)
admin.site.register(Contact)