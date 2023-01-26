from django.contrib import admin

# Register your models here.
from .models import Dog, Comment
# from .models import City,Location,State

admin.site.register(Dog)
admin.site.register(Comment)
# admin.site.register(Location)
# admin.site.register(State)
# admin.site.register(City)
