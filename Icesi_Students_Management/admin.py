from django.contrib import admin
from .models import Student
from .models import Semester
from .models import Becas
from .models import Donante
from .models import BalanceAcademico
from .models import Materia
from .models import Status
from .models import SeguimientoActividades
from .models import Actividad
from .models import User
from .models import Alerta
from .models import Roles
from .models import SeguimientoCREA
from .models import Consulta
from .models import InformacionFinanciera
from .models import SeguimientoBeca


admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Becas)
admin.site.register(Donante)
admin.site.register(BalanceAcademico)
admin.site.register(Materia)
admin.site.register(Status)
admin.site.register(SeguimientoActividades)
admin.site.register(Actividad)
admin.site.register(User)
admin.site.register(Alerta)
admin.site.register(Roles)
admin.site.register(SeguimientoCREA)
admin.site.register(Consulta)
admin.site.register(InformacionFinanciera)
admin.site.register(SeguimientoBeca)
