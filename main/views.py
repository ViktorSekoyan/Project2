from django.shortcuts import render,redirect
from .models import (
    Subscribe,headericon,Categoriesofthemonth,Categoryandfeature,
    heroandbrand,Shopsinglehtml,Shophtml,Letstalk
)
# Create your views here.

def index(request):
    headersettings = headericon.objects.first()
    categoriessettings = Categoriesofthemonth.objects.first()
    catandfea = Categoryandfeature.objects.first()
    if request.method == 'POST':
        email2 = request.POST.get('email2')
        Subscribe.objects.create(
            email2=email2
        )
        return redirect('sucess')
    return render(request, 'index.html',{
       "headersettings": headersettings,
       'categoriessettings': categoriessettings,
       'catandfea': catandfea
    })

def about(request):
    headersettings = headericon.objects.first()
    hebrand = heroandbrand.objects.first()
    return render(request, 'about.html',{
        'hebrand': hebrand,
        'headersettings': headersettings
    })

def shop(request):
    headersettings = headericon.objects.first()
    shopset = Shophtml.objects.first()
    return render(request, 'shop.html',{
        'shopset': shopset,
        'headersettings': headersettings
    })

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        Letstalk.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return redirect('sucess2')
    headersettings = headericon.objects.first()
    return render(request, 'contact.html',{
        'headersettings': headersettings
    })

def shop_single(request):
    headersettings = headericon.objects.first()
    shopsingleset = Shopsinglehtml.objects.first()
    return render(request, 'shop-single.html',{
        'shopsingleset': shopsingleset,
        'headersettings': headersettings
    })

def sucess(request):
    return render(request, 'sucess.html')

def sucess2(request):
    return render(request, 'sucess2.html')