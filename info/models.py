from django.db import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    number=models.IntegerField()
    address=models.CharField(max_length=50)
    #class Meta:
    #    db_table='test'

#python manage.py makemigration
#...migrate
#py.....shell
#from info.mogels import Student
#s1=Student(username='abc',password='abc',number=11111,address='ghhj')
#s1.save()
#s1.id
#py...
#Student.objects.all( )    ....selection records
#s1=Student.objects.get(id=2)
#s1
#S1.delete()