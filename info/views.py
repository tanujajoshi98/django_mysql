from django.shortcuts import render
from info.models import Student
from django.contrib import messages

#def home(request):
    #return render(request,'home.html')
def Insertrecord(request):
    if request.method=='POST':
        if request.POST.get('username') and request.POST.get('password') and request.POST.get('number') and request.POST.get('address'):
            saverecord=Student()
            saverecord.username=request.POST.get('username')
            saverecord.password=request.POST.get('password')
            saverecord.number=request.POST.get('number')
            saverecord.address=request.POST.get('address')
            saverecord.save()
            messages.success(request,"Record saved!!")
            return render(request,'home.html')
    else:
            return render(request,'home.html')

def recordpage(request):
    records=Student.objects.all()
    return render(request,'showrecord.html',{'records':records})


#def getdata(request):
   # if request.method=='POST':
    #    u=request.POST.['username']
    #    p=request.POST.['username']
    #    num=request.POST.['username']
    #    a=request.POST.['username']
     #   s1=modals.Student(username=u,password=p,phone=ph,address=a)



