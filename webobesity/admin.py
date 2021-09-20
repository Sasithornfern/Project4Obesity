from django.contrib import admin
from .models import NameHospital
from .models import Dobesity
from .models import diabetes
from .models import hypertention
from .models import dyslipidemia
from .models import Question
from .models import EatQuestion
from .models import exerciseQuestion

# Register your models here.

admin.site.register(NameHospital)
admin.site.register(Dobesity)
admin.site.register(diabetes)
admin.site.register(hypertention)
admin.site.register(dyslipidemia)
admin.site.register(Question)
admin.site.register(EatQuestion)
admin.site.register(exerciseQuestion)

