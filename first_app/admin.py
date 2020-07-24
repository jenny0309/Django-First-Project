from django.contrib import admin
from first_app.models import Topic, Webpage, AccessRecord, UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)