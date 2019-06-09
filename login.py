from django.shortcuts import render,redirect
from django.http import HttpResponse

def template_views(request):
    print("frist")
    return render(request,'myapp/index.html')
def login(request):
    username=request.POST.get('usr')
    password1=request.POST.get('pass')
    if username=='neeraj' and password1=='12345':
        return render(request,'myapp/home.html')
    else:
        return redirect('/login')

