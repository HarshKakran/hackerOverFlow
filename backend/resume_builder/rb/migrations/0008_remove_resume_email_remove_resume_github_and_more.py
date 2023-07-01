# Generated by Django 4.1.5 on 2023-01-21 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rb', '0007_remove_resume_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='email',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='github',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='ph',
        ),
        migrations.AddField(
            model_name='resume',
            name='contact',
            field=models.ManyToManyField(to='rb.contact'),
        ),
    ]
