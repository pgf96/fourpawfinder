from django.contrib import admin

# Register your models here.
from .models import Dog, Comment

admin.site.register(Dog)
admin.site.register(Comment)