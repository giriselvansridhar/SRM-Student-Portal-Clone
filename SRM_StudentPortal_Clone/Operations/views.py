from django.shortcuts import render


# Create your views here.



def Operation_Page(request):

    return render(request,'Operations/base.html')