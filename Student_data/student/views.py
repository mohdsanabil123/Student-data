from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

def insert( request ):
    return render( request, 'insert.html' )

def insertData( request ):
    # Data comes from HTML form
    s_id = request.POST['s_id']
    s_name = request.POST['s_name']
    s_age = request.POST['s_age']
    s_email = request.POST['s_email']
    s_contact = request.POST['s_contact']
    
    user = Student.objects.create( s_id=s_id, s_name=s_name, s_age=s_age, s_email=s_email, s_contact=s_contact )
    user.save()
    return redirect('show')

def show( request ):
    # Fetching all the data from Student table
    students_data = Student.objects.all()
    
    return render( request, 'show.html', {'data':students_data} )

def edit( request, pk ):
    data = Student.objects.get( id=pk )
    return render( request, 'edit.html', {'key':data} )

def update( request,pk ):
    udata = Student.objects.get( id=pk )
    
    udata.s_id = request.POST['s_id']
    udata.s_name = request.POST['s_name']
    udata.s_age = request.POST['s_age']
    udata.s_email = request.POST['s_email']
    udata.s_contact = request.POST['s_contact']
    # Query for update the data
    udata.save()
    return redirect('show')

# Delete particular student data

def destroy( request, pk ):
    d_data = Student.objects.get( id=pk )
    d_data.delete()
    return redirect('show')