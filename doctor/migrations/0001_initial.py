# Generated by Django 2.1.5 on 2019-06-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dr_first_name', models.CharField(max_length=10)),
                ('dr_middle_name', models.CharField(max_length=10)),
                ('dr_last_name', models.CharField(max_length=10)),
                ('gender', models.BooleanField(choices=[('male', 'male'), ('female', 'female')])),
                ('dr_image', models.ImageField(upload_to='pic_folder/')),
                ('dr_phone_no', models.CharField(max_length=10)),
                ('dr_mail', models.EmailField(max_length=254)),
                ('dr_degree', models.CharField(choices=[('MBBS', 'MECICAL'), ('MD', 'DOCTOR OF MEDICINE'), ('DO', 'DOCTOR OF OSTEOPATHIC MEDICINE')], max_length=15)),
                ('dr_speciality', models.CharField(max_length=50)),
                ('address', models.CharField(choices=[('ahmedabad', 'ahmedabad'), ('baroda', 'baroda'), ('palanpur', 'palanpur'), ('gandhinagar', 'gandhinagar'), ('unjha', 'unjha'), ('mehsana', 'mehsana')], max_length=20)),
            ],
        ),
    ]
