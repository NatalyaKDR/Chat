from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render

from chat.forms import AuthForm


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

#Пользовательская часть
class MyLoginView(LoginView): #login
    template_name= 'chat/login.html'
    redirect_authenticated_user = False

class MyLogoutView(LogoutView): #logout
    next_page='/chat'


'''#функция авторизаци
def login_view(request):
    if request.method =="POST":
        auth_form=AuthForm(request.POST)
        if auth_form.is_valid():
            username=auth_form.cleaned_data['username']
            password=auth_form.cleaned_data['password']
            user=authenticate(username=username,password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Вы вошли в систему")
                else:
                    auth_form.add_error('__all__', "Ошибка. Учетная запись не активна")
            else:
                auth_form.add_error("__all__", "Ошибка! Проверьте логин и пароль")
    else:
        auth_form=AuthForm()

    context={'form':auth_form}
    return render (request, 'chat/login.html', context=context)'''