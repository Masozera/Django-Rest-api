from django.contrib import admin
from .models import Lesson, HomePageFormModel
# Register your models here.

admin.site.register(Lesson),
admin.site.register(HomePageFormModel)