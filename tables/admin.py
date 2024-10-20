from django.contrib import admin
from .models import Hospital,Organ,Donor,Doctor,Driver,Department,Insurance,Patient,ConsentForm,MedicalReport,Consults,Transport,OrganTransplant
from .models import LoginInfo

admin.site.register(LoginInfo)

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Donor)
admin.site.register(Insurance)
admin.site.register(Patient)
admin.site.register(ConsentForm)
admin.site.register(MedicalReport)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Consults)
admin.site.register(Driver)
admin.site.register(Transport)
admin.site.register(Organ)
admin.site.register(OrganTransplant)

