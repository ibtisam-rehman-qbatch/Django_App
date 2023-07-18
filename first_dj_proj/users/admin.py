from django.contrib import admin
from .models import User

class displayDetails(admin.ModelAdmin):
    list_display=("firstName", "phone")

admin.site.register(User,displayDetails)

# Register your models here.
