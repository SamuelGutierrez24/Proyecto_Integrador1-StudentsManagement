from django.contrib import admin
from .models import Carrera
from .models import Becas
from .models import Student
from .models import Materia
from .models import Status
from .models import Semester
from .models import SeguimientoBeca
from .models import InformacionFinanciera
from .models import Actividad
from .models import AsistenciasActividad
from .models import BalanceAcademico
from .models import Nota
from .models import Donante
from .models import User
from .models import Alerta


admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Becas)
admin.site.register(Donante)
admin.site.register(BalanceAcademico)
admin.site.register(Materia)
admin.site.register(Status)
admin.site.register(Actividad)
admin.site.register(User)
admin.site.register(Alerta)
admin.site.register(Carrera)
admin.site.register(InformacionFinanciera)
admin.site.register(SeguimientoBeca)
admin.site.register(AsistenciasActividad)
admin.site.register(Nota)
