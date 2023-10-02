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
# from Icesi_Students_Management.views.home import home
# from Icesi_Students_Management.views.signin import Signin
# from Icesi_Students_Management.views.signout import Signout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Icesi_Students_Management.urls'))
    # path('', home, name='home'),
    # path('signup/', signup, name='signup'),
    # path('tasks/', Views.tasks, name='tasks'),
    # path('signin/', Signin.as_view , name='singin'),
    # path('logout/', signout, name='logout'),
]
