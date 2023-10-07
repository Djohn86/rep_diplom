from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import NewsForm
from .models import Sportnews


def allnews(request):
    an = Sportnews.objects.order_by('-created')
    return render(request, 'newpost/allnews.html', {'an': an})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'newpost/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('mynews')
            except IntegrityError:
                return render(request, 'newpost/signupuser.html', {
                    'form': UserCreationForm(),
                    'error': 'Такой пользователь существует. Придумайте другое имя'})
        else:
            return render(request, 'newpost/signupuser.html', {
                'form': UserCreationForm(),
                'error': 'Пароли не совпадают'})

def mynews(request):
    np = Sportnews.objects.filter(user=request.user)
    return render(request, 'newpost/mynews.html', {'np': np})


# def football(request):
#     foot = Sportnews.objects.filter()


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('allnews')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'newpost/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'newpost/loginuser.html', {'form': AuthenticationForm()},
                          'error' 'учетной записи не существует ')
        else:
            login(request, user)
            return redirect('mynews')


def createnews(request):
    if request.method == 'GET':
        return render(request, 'newpost/createnews.html', {'form': NewsForm()})
    else:
        try:
            form = NewsForm(request.POST)
            newpost = form.save(commit=False)
            newpost.user = request.user
            newpost.save()
            return redirect('mynews')
        except ValueError:
            return render(request, 'newpost/createnews.html', {
                'form': NewsForm(),
                'error': 'Переданы не верные данныеБ введите снова.'
            })


def tennis(request):
    an = Sportnews.objects.order_by('-created')
    return render(request, 'newpost/tennis.html', {'an': an})


def football(request):
    an = Sportnews.objects.order_by('-created')
    return render(request, 'newpost/football.html', {'an': an})


def hockey(request):
    an = Sportnews.objects.order_by('-created')
    return render(request, 'newpost/hockey.html', {'an': an})


def basketball(request):
    an = Sportnews.objects.order_by('-created')
    return render(request, 'newpost/basketball.html', {'an': an})


def voleyball(request):
    an = Sportnews.objects.order_by('-created')
    return render(request, 'newpost/voleyball.html', {'an': an})


def box(request):
    an = Sportnews.objects.order_by('-created')
    return render(request, 'newpost/box.html', {'an': an})


def detail(request, blog_id):
    post = get_object_or_404(Sportnews, pk=blog_id)
    return render(request, 'newpost/detail.html', {'post': post })
