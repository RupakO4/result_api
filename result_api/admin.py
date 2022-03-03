from django.contrib import admin

# Register your models here.
from .models import Exam, Result
admin.site.register(Exam)
admin.site.register(Result)