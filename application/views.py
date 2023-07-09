from django.shortcuts import render

# Create your views here.
from application.models import *
from application.serilazer import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy
from application.forms import * 
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response



def home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')



def userregistration(request):
    uf = UserForm()
    d={'uf':uf}
    if request.method == 'POST':
        ufd = UserForm(request.POST)
        if ufd.is_valid():
            ufdo = ufd.save(commit=False)
            ufdo.set_password(ufd.cleaned_data['password'])
            ufdo.save()

           
            return HttpResponse("Registration is successfully!!!....")
        else:
            return HttpResponse("NOT Registered or INvalid DAta.....")
    return render(request,'userregistration.html',d)





def user_login(request):
    if request.method == 'POST':

        username=request.POST['username']
        password=request.POST['password']

        AUO = authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("data is invalid ")
        

    return render(request,'user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def FoodCreate(request):
    d={'UO':Food_blogForm()}
    if request.method == 'POST':
        UOF =Food_blogForm(request.POST)
        if UOF.is_valid():
            UOF.save()
            return HttpResponse("Data is inserted Successfully")
        else:
            return HttpResponse('not valid')
    return render(request,'FoodCreate.html',d)


class FoodData(ViewSet):
    def list(self,request):
        AD=Food_blog.objects.all()
        SD=FoodForm(AD,many=True)
        d={'data':SD.data}
        return render(request,'list.html',d)

    def retrieve(self,request,pk):
        TO=Food_blog.objects.get(pk=pk)
        SDO=FoodForm(TO)
        return Response(SDO.data)
        d1={'DOdata':SDO.data}
        return render(request,'retrieve.html',d1)


    def update(self,request,pk):
        SP=Food_blog.objects.get(pk=pk)
        SP=FoodForm(SP,data=request.data)
        if SP.is_valid():
            SP.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=Food_blog.objects.get(pk=pk)
        SPD=FoodForm(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
    def destroy(self,request,pk):
        Food_blog.objects.get(pk=pk).delete()
        return Response({'Deleted':'Product is deleted'})
    
