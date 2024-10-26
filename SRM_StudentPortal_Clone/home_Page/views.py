from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

def Home_Page(request):
    if request.method == "POST":
        Net_ID = request.POST.get('netid')
        Password = request.POST.get('password')
        print(Net_ID)
        print(Password)
    return render(request, 'home_Page/homepage.html')
