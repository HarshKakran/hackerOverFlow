import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Resume(models.Model):

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)

    skills = ArrayField(
        models.CharField(
            max_length=512, null=True, blank=True,
        ), null=True, blank=True, help_text="Array containing skills of the user"
    )
    achievements = ArrayField(
        models.TextField(null=True, blank=True), null=True, blank=True, help_text='achievements'
    )

    projects = models.ManyToManyField('Project', help_text="link to the projects of the user")
    contact = models.ManyToManyField('Contact')
    education = models.ManyToManyField('Education')
    workx = models.ManyToManyField('WorkX')
    languages = models.ManyToManyField('Languages')

class Languages(models.Model):
    name = models.CharField(max_length=120)

class Contact(models.Model):
    PLATFORM_GITHUB = 'github'
    PLATFORM_LINKEDIN = 'linkedin'
    PLATFORM_EMAIL = 'email'
    PLATFORM_PH = 'ph'

    PLATFORM_CHOICES = (
        (i, i) for i in [PLATFORM_PH, PLATFORM_EMAIL, PLATFORM_LINKEDIN, PLATFORM_GITHUB])


    user = models.ForeignKey('User', on_delete=models.CASCADE)
    platform = models.CharField(
        max_length=128, null=True, blank=True, choices=PLATFORM_CHOICES)
    url = models.CharField(max_length=512)

class Education(models.Model):
    YEAR_CHOICES = (
        (i, i) for i in range(1980, datetime.datetime.now().year+1)
    )

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    programme = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    s_yr = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    e_yr = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    cgpa = models.IntegerField(default=5)

class WorkX(models.Model):
    YEAR_CHOICES = (
        (i, i) for i in range(1980, datetime.datetime.now().year + 1)
    )

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    role = models.CharField(max_length=512)
    org = models.CharField(max_length=512)
    desc = models.TextField(null=True, blank=True)
    s_yr = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    e_yr = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)

class Project(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=512)