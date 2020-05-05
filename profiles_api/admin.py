from django.contrib import admin
from profiles_api import models

### This tells the Django admin to register our UserProfile model with the admin
### site so it is accesible through the admin interface
admin.site.register(models.UserProfile)
