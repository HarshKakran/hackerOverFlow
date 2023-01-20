from django.contrib import admin
from .models import Resume, WorkX, Languages, Contact, Education, Project

# Register your models here.
admin.site.register(WorkX)
admin.site.register(Resume)
admin.site.register(Languages)
admin.site.register(Contact)
admin.site.register(Education)
admin.site.register(Project)