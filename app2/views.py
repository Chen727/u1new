from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def html(request):
   # string = u'is now'
   # return render(request, 'html1.html', {'string': string})
   TutorialList=["html","css","jquery"]
   return render(request,'html1.html',{'TutorialList':TutorialList})
