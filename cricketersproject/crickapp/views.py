from django.shortcuts import render, redirect
from . models import Cricketers
from django.http import HttpResponse
from . form import Cricketersform



def index(request):
    cricketers=Cricketers.objects.all()
    context={'cricketers_list':cricketers}
    return render(request,'index.html',context)




def detail(request,cricketers_id):
    cricketers=Cricketers.objects.get(id=cricketers_id)
    return render(request,"detail.html",{'cricketers':cricketers})

def add_cricketers (request):
    if request.method == "POST":
        name = request.POST.get('name')
        skill = request.POST.get('skill')
        year = request.POST.get('year')
        img = request.FILES['img']
        cricketers = Cricketers(name=name, skill=skill, year=year, img=img)
        cricketers.save()
    return render(request,'add.html')


def update(request,id):
    cricketers= Cricketers.objects.get(id=id)
    form = Cricketersform(request.POST or None,request.FILES,instance=cricketers)
    if form.is_valid():
        form.save()
        return redirect ('/')
    return render(request,'edit.html',{'form':form,'cricketers':cricketers})

def delete(request,id):
    if request.method =='POST':
        cricketers=Cricketers.objects.get(id=id)
        cricketers.delete()
        return redirect('/')
    return  render(request,'delete.html')