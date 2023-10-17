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
from django.urls import path, include
#import Icesi_Students_Management.views.views as views
from django.conf import settings
from django.conf.urls.static import static
from Icesi_Students_Management.views import menuConta
from Icesi_Students_Management.views import infoFinanciera
from Icesi_Students_Management.views import buscarEstud
from Icesi_Students_Management.views import modificar
import Icesi_Students_Management.views.bumenu as buMenu
import Icesi_Students_Management.views.registroActividades as registroA


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home, name='home'),
    #path('signup/', views.signup, name='signup'),
    #path('tasks/', views.tasks, name='tasks'),
    #path('signin/', views.signin, name='singin'),
    #path('logout/', views.signout, name='logout'),
    path('contabilidad/', menuConta.menu, name='menuContabilidad'),
    path('contabilidad/eliminar-noti/<id>/', menuConta.eliminar_noti, name='eliminar_noti'),
    path('contabilidad/ver-noti/<int:id>/', menuConta.ver_noti, name='ver_noti'),
    path('contabilidad/infoFinanciera.html', infoFinanciera.infoFinanciera, name='infoFinanciera'),
    path('contabilidad/buscarEstud.html', buscarEstud.menuBuscar, name='buscarEstud'),
    path('contabilidad/modificar.html/<str:code>/', modificar.modificarInfo, name='modificarInfo'),
    path('contabilidad/eliminar-estudiante/<str:code>/', buscarEstud.eliminar_estudiante, name='eliminar_estudiante'),
    path('bienestarUniversitario/',buMenu.menu, name='bienestarUniversitario'),
    path('bienestarUniversitario/registroActividades',registroA.registroA, name='registroActividades'),
    path('', include('Icesi_Students_Management.urls'))

]
