from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, redirect
from django.contrib import auth

@csrf_protect
def login(request):
    args = {}
    args.update(request)
    if request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user=auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                args['login_error']= "Пользователь ненайден"
                return  render_to_response('login.html', args)
    else:
            return render_to_response('login.html', args)
@csrf_protect

def logout(request):
    auth.logout(request)
    return redirect('/')