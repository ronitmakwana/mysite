# Generated by Django 2.1.5 on 2019-06-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='password1',
            field=models.CharField(default='12344', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='password2',
            field=models.CharField(default='12344', max_length=50),
        ),
    ]
