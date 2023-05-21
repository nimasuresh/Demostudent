from django.contrib import admin

# Register your models here
from credentials.models import Department, Courses,Purpose


admin.site.register(Department)
admin.site.register(Courses)
admin.site.register(Purpose)