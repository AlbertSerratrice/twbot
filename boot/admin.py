from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(TweetLookUpWord)
admin.site.register(TweetLookUpBadWord)
admin.site.register(OutBoundDirectMessage)
admin.site.register(TweetLookUpCoordinates)