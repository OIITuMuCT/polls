from django.contrib import admin
from .models import Division
from .models import Employee
from .models import PersonalInfo
from .models import LearningCourse

# Register your models here.
admin.site.register(Division)
admin.site.register(Employee)
admin.site.register(PersonalInfo)
admin.site.register(LearningCourse)