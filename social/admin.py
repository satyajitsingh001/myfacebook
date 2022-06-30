from django.contrib import admin
from social.models import UserPost, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserPost)

