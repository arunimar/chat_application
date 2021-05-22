from django.http import HttpResponse
from django.shortcuts import render
from core.models import User


# Create your views here.

def dashboard_view(request, *args, **kwargs):
    return HttpResponse('qwert')


def login_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return HttpResponse('Success')
            else:
                return HttpResponse('Fail')
        except:
            return HttpResponse('User not found!')
