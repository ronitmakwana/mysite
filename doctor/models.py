from django.db import models

# Create your models here.
class doctor(models.Model):
    dr_first_name=models.CharField(max_length=10)
    dr_middle_name=models.CharField(max_length=10)
    dr_last_name=models.CharField(max_length=10)
    ch=(
        ('male','male'),
        ('female','female')
    )
    gender=models.CharField(max_length=10,choices=ch)
    dr_image=models.ImageField(upload_to = 'pic_folder/',)
    dr_phone_no=models.CharField(max_length=10)
    dr_mail=models.EmailField()
    #(name of the choice,this name is for dropdown)
    DR_DEGREE=(
                ('MBBS','MECICAL'),
                ('MD','DOCTOR OF MEDICINE'),
                ('DO','DOCTOR OF OSTEOPATHIC MEDICINE')
            )
    dr_degree=models.CharField(max_length=15,choices=DR_DEGREE)
    dr_speciality=models.CharField(max_length=50)
    ahmedabad='ahmedabad'
    baroda='baroda'
    palanpur='palanpur'
    gandhinagar='gandhinagar'
    unjha='unjha'
    mehsana='mehsana'
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
        return self.dr_first_name

