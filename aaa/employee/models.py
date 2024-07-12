from django.db import models

class Employee(models.Model):
    empcode = models.TextField(max_length=4, db_column='EMPCODE')
    username = models.CharField(max_length=100, db_column='USER NAME')
    department = models.CharField(max_length=100, db_column='DEPT NAME')
    qualification = models.CharField(max_length=100,db_column='HIGHESTQUALIFICATION')
    email = models.EmailField(max_length=100,db_column='EMAIL')
    designation = models.CharField(max_length=15,db_column='DESIGNATION')
    mobile = models.CharField(max_length=15,db_column='MOBILE')
    extension = models.CharField(max_length=15,db_column='EXTENSION')
    gender = models.TextField(max_length=10,db_column='SEX')
    dob = models.DateField(max_length=10,blank=True, null=True,db_column='DOB')
    img_brief = models.ImageField(upload_to='static/img',db_column='IMG')
    # image_major = models.ImageField(null=True)
   
    class Meta:
        db_table = 'userlogin'

    def __str__(self):
        return self.empcode
    
class Comment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
