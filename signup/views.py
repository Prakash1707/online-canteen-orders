from django.shortcuts import render
from django.http import HttpResponse
from .models import details
from .models import foodItem
from .models import cart
from .models import transactions
import uuid
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request,'signup/index.html')

def signin(request):
    return render(request,'signup/login.html')

def register(request):
    return render(request,'signup/register.html')

def home(request):
    bf=foodItem.objects.filter(typeof__exact='breakfast')
    lch=foodItem.objects.filter(typeof__exact='lunch')
    sck=foodItem.objects.filter(typeof__exact='snacks')
    return render(request,'signup/home.html',{'bf':bf,'lch':lch,'sck':sck})
    

def verify(request):
    details_inst=details()
    details_inst.firstName=request.POST.get('fname')
    details_inst.lastName=request.POST.get('lName')
    details_inst.phone=request.POST.get('phNo')
    details_inst.gender=request.POST.get('gender')
    details_inst.email=request.POST.get('email')
    details_inst.username=request.POST.get('uName')
    details_inst.password=request.POST.get('pWord')
    cPass=request.POST.get('cPWord')
    if(details_inst.password==cPass):
        details_inst.save()
        return render(request,'signup/login.html')
    return render(request,'signup/register.html')

def login(request):
    user=request.POST.get('uName')
    passw=request.POST.get('pass')
    users=details.objects.get(username__exact=user)
    npass=users.password
    if npass==passw:
        bf=foodItem.objects.filter(typeof__exact='breakfast')
        lch=foodItem.objects.filter(typeof__exact='lunch')
        sck=foodItem.objects.filter(typeof__exact='snacks')
        return render(request,'signup/home.html',{'bf':bf,'lch':lch,'sck':sck})
    else:
        return render(request,'signup/login.html')

def cartp(request):
    fi=foodItem.objects.all()
    sum=0
    id=uuid.uuid4()
    for i in fi:
        cartd=cart()
        cartd.name=i.name
        cartd.typeof=i.typeof
        cartd.price=int(i.price)
        cartd.transcid=id
        quant=int(request.POST.get(i.name))
        if(quant>0):
            cartd.quantity=quant
            sum+=(i.price)*quant
            cartd.save()
    allcart=cart.objects.filter(transcid__exact=id)
    completed=transactions()
    completed.total=sum
    completed.transactionId=id
    completed.save()
    return render(request,'signup/cart.html',{'list':allcart,'total':sum,'id':id})

def cmplt(request):
    name=request.POST.get('uname')
    to=request.POST.get('to')
    fromm=request.POST.get('from')
    id=request.POST.get('id')
    bill=request.POST.get('bill')
    li=[to,fromm,]
    msg=name+' '+bill+' '+id
    send_mail('thank you',msg,fromm,li,fail_silently=False)
    return render(request,'signup/index.html')

def aboutus(request):
    return render(request,'signup/aboutus.html')
    

    
        
