from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
async def say_hello(request):
    # pull data from database
    # transform
    x = await calculate()
    
    return render(request, 'hello.html', {'name':"Ma-aruf"})
    # return HttpResponse('Hello World!')

async def calculate():
    x = 1 
    y = 2
    return x 