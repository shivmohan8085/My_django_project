from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse
from .models import Emp



# selet all data
def emp_home(request):
    emp_data =Emp.objects.all()
    return render(request,"emp/emp_home.html", {'emp_data':emp_data})



# insert data
def add_emp(request):
    if request.method=="POST" :
        print("data is comming")
        
        # data fetch
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        # Create model object and set the data
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if e.working is None :
            e.working = False
        else :
            e.working = True
        e.save()

        return redirect("/emp/home")

    return render(request, 'emp/add_emp.html',{})


#delete data
def delete_emp(request,emp_id):
    emp = Emp.objects.get(id=emp_id)
    emp.delete()
    print(emp_id, ": deleted successfully")
    # emp = get_object_or_404(Emp, pk=emp_id)
    # emp.delete()
    return redirect("/emp/home/")

def update_emp(request,e_id):
    emp = Emp.objects.get(id=e_id)
    return render(request,'emp/update_emp.html',{'emp':emp})


def do_update_emp(request, e_id):
    if request.method=="POST" :
        print("data is comming")
        
        # data fetch
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

    

        # Create model object and set the datass 
        e = Emp.objects.get(id=e_id)
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department

        if emp_working is None:
            e.working = False
        else :
            e.working = True
        e.save()
    return redirect("/emp/home/")

