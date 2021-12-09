from django.contrib import admin
from . import models

# Makes this accessible through the admin interface
admin.site.register(models.UserProfile)
