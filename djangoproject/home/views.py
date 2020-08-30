from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contect
from django.contrib import messages
# Create your views here.
def index(request):
   # context ={
    #    'variable':'Avi',
     #   'A':'Sohan'
    #}
    #return HttpResponse("This is HomePage Welcome to new user It is created by Avi..")
    return render(request,'index.html')
def about(request):
    return HttpResponse("This is about page")
def services(request):
    return HttpResponse("Serves details you can't login without autheticatication")
def contect(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        quarry=request.POST.get('quarry')
        contect=Contect(name=name,email=email,quary=quarry,date=datetime.today())
        contect.save() 
        messages.success(request, 'Your message has been send !')
    #return HttpResponse("For contect me call 9060071846")
    return render(request,'contect.html')
def new_adm(request):
    return render(request ,'text.html')
def collage_infra(request):
    return render(request,'collage_infra.html')
def branch(request):
    return render(request,'branch.html')
def alu_con(request):
    return render(request,'alu_con.html')

