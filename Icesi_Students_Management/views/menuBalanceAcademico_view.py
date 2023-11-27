from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required


def rol_check(user):
    return user.rol == 5
def menuBalanceAcademico(request):
    return render(request, 'menuBalanceAcademico.html')