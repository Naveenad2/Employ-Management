from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#add to the database that how many jo department is there


class Job_department(models.Model):
    

    job_department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.job_department_name 



class Manager(models.Model):

    #add the connection that manager is a user to the software
    connection = models.OneToOneField(User,on_delete=models.CASCADE)

    manager_name =models.CharField(max_length=50)
    email=models.CharField(max_length=100,null=True)
    phone_number=models.IntegerField()
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    date_of_birth=models.DateField()

    def __str__(self):
        return self.manager_name


class Employee(models.Model):

      # add the connection that employee is a user 
    connection=models.OneToOneField(User,on_delete=models.CASCADE)

    employee_name =models.CharField(max_length=50)
    email=models.CharField(max_length=100,null=True)
    
     # add where the employee is going to work
    job_department = models.ForeignKey(Job_department,on_delete=models.CASCADE,null=True)

    phone_number=models.IntegerField()
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    date_of_birth=models.DateField()

    start_time = models.CharField(max_length=50,null=True)
    end_time = models.CharField(max_length=50,null=True)



    def __str__(self):
        return self.employee_name
    









