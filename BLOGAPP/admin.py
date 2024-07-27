from django.contrib import admin
from BLOGAPP.models import *

admin.site.register(Post)
admin.site.register(UserBio)

# class UserProfileAdmin:
#     list_display = ['fname', 'lname', 'gender']
# Register your models here.