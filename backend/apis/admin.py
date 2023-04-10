from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(books)
admin.site.register(courses)
admin.site.register(course_offer_university)

