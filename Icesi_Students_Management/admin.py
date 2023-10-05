from django.contrib import admin
from .models import Student
from .models import Becas
from .models import Donante
from .models import User
from .models import Alerta

admin.site.register(Student)
admin.site.register(Becas)
admin.site.register(Donante)
admin.site.register(User)
admin.site.register(Alerta)