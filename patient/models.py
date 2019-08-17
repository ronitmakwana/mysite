from django.db import models

# Create your models here.
class patient(models.Model):
    first_name=models.CharField(max_length=10)
    middle_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    image=models.ImageField(upload_to = 'pic_folder/',)
    phone_no=models.CharField(max_length=10)
    mail=models.EmailField()
    ahmedabad='ahmedabad'
    baroda='baroda'
    palanpur='palanpur'
    gandhinagar='gandhinagar'
    unjha='unjha'
    mehsana='mehsana'
    #(name of the choice,this name is for dropdown)
    city=(
        (ahmedabad,'ahmedabad'),
        (baroda,'baroda'),
        (palanpur,'palanpur'),
        (gandhinagar,'gandhinagar'),
        (unjha,'unjha'),
        (mehsana,'mehsana')
    )
    address=models.CharField(max_length=20,choices=city)
    password1=models.CharField(max_length=50,default='12344')
    password2=models.CharField(max_length=50,default='12344')
    def __str__(self):
        return self.first_name

