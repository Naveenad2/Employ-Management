from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.http import HttpResponse

# Create your views here.
def main_page(request):

    if (request.user.id is not None):
        
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if(Employee.objects.filter(employee_name = user.username).exists()):
             
             return redirect("/EmployeeMainPage")
        
        if(Manager.objects.filter(manager_name = user.username).exists()):
             
             return redirect("/managerMainPage")
        
    else:

       return render(request,'main.html')

def Employeelogin(request):
     
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('EmployeeMainPage')
        else:
            return HttpResponse("Wrong password")
        
     return render(request,'employeelogin.html')
 

 

def Managementlogin(request):
     
      if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('managerMainPage')
        else:
            return HttpResponse("Wrong password")
        
      return render(request,'managementlogin.html')

 

def employee_reg(request):
    return render(request,'employee_reg.html')

def management_reg(request):
     
      return render(request,'managerRegistration.html')
     

def employee_auth(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    phno=request.POST.get('phno')
    age=request.POST.get('age')
    address=request.POST.get('address')
    dob=request.POST.get('dob')
    password=request.POST.get('password')
    repeatpass=request.POST.get('repassword')

    if password == repeatpass:

            user = User.objects.filter(username=name)
            isuser = user.exists()
            if isuser is False:
                new_user = User.objects.create_user(username=name,password=password)
                new_user.save()


                #save the user
            employee = Employee(
            connection =new_user,
            employee_name=name,
            email=email,
            phone_number=phno,
            age=age,
            address=address,
            date_of_birth=dob
        )
            
            employee.save()

            authuser = authenticate(username=name,password=password)
            login(request,authuser)

    else:
         render(request,'employee_reg.html')

    
    return redirect('/EmployeeMainPage')

def management_auth(request):

    name=request.POST.get('name')
    email=request.POST.get('email')
    phno=request.POST.get('phno')
    age=request.POST.get('age')
    address=request.POST.get('address')
    dob=request.POST.get('dob')
    password=request.POST.get('password')
    repeatpass=request.POST.get('repassword')

    if password == repeatpass:

            user = User.objects.filter(username=name)
            isuser = user.exists()
            if isuser is False:
                new_user = User.objects.create_user(username=name,password=password)
                new_user.save()


                #save the user
            manager = Manager(
            connection =new_user,
            manager_name=name,
            email=email,
            phone_number=phno,
            age=age,
            address=address,
            date_of_birth=dob
        )
            
            manager.save()

            authuser = authenticate(username=name,password=password)
            login(request,authuser)

    else:
         render(request,'management_reg.html')

    return redirect('/managerMainPage')


def managerMainPage(request):
     
     user_id = request.user.id
     try:
          manager = Manager.objects.get(connection__id=user_id)
   
          print(manager.manager_name)
     except Manager.DoesNotExist:
  
          print("Employee not found")
     

     return render(request,'managerMainPage.html',{"user":manager})



def managerSaveChanges(request):
     user_id = request.user.id
     try:
          manager = Manager.objects.get(connection__id=user_id)
   
       
     except Manager.DoesNotExist:
  
          print("manager not found")

     if request.method == 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            phno=request.POST.get('phno')
            age=request.POST.get('age')
            address=request.POST.get('address')
           
            manager.manager = name
            manager.email = email
            manager.phone_number = phno
            manager.age = age
            manager.address = address

            manager.save()
          
     
     return render(request,"managerSaveChanges.html",{"user":manager})


def viewAllEmployees(request):
     employees = Employee.objects.all()

     return render(request,"ViewAllEmployee.html",{"employees":employees})
     
def updateEmployeeProfileByManager(request,id):
     

     employee = Employee.objects.get(id=id)
     
     return render(request,"UpdateEmployeeTimeShift.html",{"employee":employee})



def updateEmployeePOST(request):
     
      if request.method == 'POST':
        department = request.POST.get('department')
        starttime = request.POST.get('stime')
        endtime = request.POST.get('etime')
        userid = request.POST.get('userid')

        employee = Employee.objects.get(id=userid)

        depobject = Job_department(job_department_name=department)
        depobject.save()

        employee.start_time = starttime
        employee.end_time = endtime
        employee.job_department = depobject

        employee.save()
      return redirect("viewAllEmployees")


def EmployeeMainPage(request):
     user_id = request.user.id
     try:
          employee = Employee.objects.get(connection__id=user_id)
   
          print(employee.employee_name)
     except Employee.DoesNotExist:
  
          print("Employee not found")
     

     return render(request,"EmployeeMainPage.html",{"user":employee})


def EmployeeSaveChanges(request):
     
     user_id = request.user.id
     try:
          employee = Employee.objects.get(connection__id=user_id)
   
          print(employee.employee_name)
     except Employee.DoesNotExist:
  
          print("Employee not found")

     if request.method == 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            phno=request.POST.get('phno')
            age=request.POST.get('age')
            address=request.POST.get('address')
           
            employee.employee_name = name
            employee.email = email
            employee.phone_number = phno
            employee.age = age
            employee.address = address

            employee.save()

            return redirect("/EmployeeMainPage")
          
     
     return render(request,"EmployeeSaveChanges.html",{"user":employee})

def Sregisteration(request):
     
      if (request.user.id is not None):
        
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if(Employee.objects.filter(employee_name = user.username).exists()):
             
             return redirect("/EmployeeMainPage")
        
        if(Manager.objects.filter(manager_name = user.username).exists()):
             
             return redirect("/managerMainPage")
        
      else:
     
            return  render(request,'selectRegistration.html')

def Slogin(request):
       

        if (request.user.id is not None):
            
            user_id = request.user.id
            user = User.objects.get(id=user_id)

            if(Employee.objects.filter(employee_name = user.username).exists()):
                
                return redirect("/EmployeeMainPage")
            
            if(Manager.objects.filter(manager_name = user.username).exists()):
                
                return redirect("/managerMainPage")
            
        else:
        
              return  render(request,'Slogin.html')


def Logout_(request):
       logout(request)
       return redirect("/")