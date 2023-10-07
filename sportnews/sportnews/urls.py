"""
URL configuration for sportnews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  django.conf.urls.static import static
from django.conf import settings
from newpost import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth личный кабинет
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    # страница своих опубликованных новостей
    path('', views.allnews, name='allnews'),
    path('mynews/', views.mynews, name='mynews'),
    path('create/', views.createnews, name='createnews'),

    # фильтры
    path('tennis/', views.tennis, name='tennis'),
    path('football/', views.football, name='football'),
    path('hockey/', views.hockey, name='hockey'),
    path('basketball/', views.basketball, name='basketball'),
    path('voleyball/', views.voleyball, name='voleyball'),
    path('box/', views.box, name='box'),

    # отображение полной новости
    path('<int:blog_id>/', views.detail, name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)