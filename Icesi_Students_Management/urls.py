from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('BalanceAcademico/', views.BAMenu.menu, name='menuBalanceAcademico'),
    path('BalanceAcademico/buscarEstudiante.html', views.buscarEstudiante_view.buscarEstudiante, name='buscarEstudiante'),
    path('BalanceAcademico/registroNotasBA.html', views.RegMateria, name='registroNotasBA')
]