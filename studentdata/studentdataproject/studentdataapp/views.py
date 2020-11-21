from django.shortcuts import render,redirect
from .models import StudentData

def student_data_view(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        telugu = request.POST.get('telugu')
        hindi = request.POST.get('hindi')
        english = request.POST.get('english')
        maths = request.POST.get('maths')
        science = request.POST.get('science')
        social = request.POST.get('social')

        data = StudentData(
            first_name = fname,
            last_name = lname,
            mobile_number = mobile,
            telugu = telugu,
            hindi = hindi,
            english = english,
            maths = maths,
            science = science,
            social = social
        )
        data.save()
        students = StudentData.objects.all()
        return render(request,'student_data_inserting.html',{'students':students})
    else:
        students = StudentData.objects.all()    #[]
        return render(request,'student_data_inserting.html',{'students':students})


#GET---> OPen form with data
def update_stduent_data(request,id):
    student = StudentData.objects.get(id=id)
    return render(request,'student_data_updating.html',{'student':student})


#POST ---> Saving Updated Data
def updated_data_save(request,id):
    student = StudentData.objects.get(id=id)
    student.first_name = request.POST.get('fname')
    student.last_name = request.POST.get('lname')
    student.mobile_number = request.POST.get('mobile')
    student.telugu = request.POST.get('telugu')
    student.hindi = request.POST.get('hindi')
    student.english = request.POST.get('english')
    student.maths = request.POST.get('maths')
    student.social = request.POST.get('social')
    student.science = request.POST.get('science')
    student.save()
    return redirect('/')





def delete_student_data(request,id):
    student = StudentData.objects.get(id=id)
    student.delete()
    return redirect('/')














