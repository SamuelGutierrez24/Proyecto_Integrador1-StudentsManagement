from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator


@login_required
def home(request):
    return render(request, 'home.html')
