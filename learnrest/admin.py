from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Snippet)
admin.site.register(JobApplication)
admin.site.register(JobPositions)