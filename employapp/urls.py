"""employmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.main_page,name='main'),
    
    path('Employeelogin',views.Employeelogin,name='Employeelogin'),

    path('Managementlogin',views.Managementlogin,name='Managementlogin'),
   
    path('employee_reg',views.employee_reg,name='employee_reg'),

    path('management_reg',views.management_reg,name='employee_reg'),

    path('employee_auth',views.employee_auth,name='employee_auth'),

    path('management_auth',views.management_auth,name="management_auth"),

    path('Sregisteration',views.Sregisteration,name='Sregisteration'),

    path('EmployeeMainPage',views.EmployeeMainPage,name='EmployeeMainPage'),

    path('managerMainPage',views.managerMainPage,name="managerMainPage"),

    path('EmployeeSaveChanges',views.EmployeeSaveChanges,name='EmployeeSaveChanges'),

    path('managerSaveChanges',views.managerSaveChanges,name="managerSaveChanges"),

    path('viewAllEmployees',views.viewAllEmployees,name="viewAllEmployees"),

    path('updateEmployeeProfile/<int:id>',views.updateEmployeeProfileByManager,name="updateEmployeeProfile"),

     path('updateEmployeePOST',views.updateEmployeePOST,name="updateEmployeePOST"),

    path('Slogin',views.Slogin,name='Sregisteration'),

    path('logout',views.Logout_,name="logout")
  

]
