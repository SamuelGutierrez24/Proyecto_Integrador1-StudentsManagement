"""
URL configuration for Students_Management project.

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
from Icesi_Students_Management.views import menuConta
from Icesi_Students_Management.views import views
from Icesi_Students_Management.views import infoFinanciera
from Icesi_Students_Management.views import buscarEstud


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('signin/', views.signin, name='singin'),
    path('logout/', views.signout, name='logout'),
    path('contabilidad/', menuConta.menu, name='menuContabilidad'),
    path('contabilidad/infoFinanciera.html', infoFinanciera.infoFinanciera, name='infoFinanciera'),
    path('contabilidad/buscarEstud.html', buscarEstud.menuBuscar, name='buscarEstud')

]
