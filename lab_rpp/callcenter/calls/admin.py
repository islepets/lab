from django.contrib import admin
from .models import Client, Reason, Operator, Status, Call

# Register your models here.

admin.site.register(Client)
admin.site.register(Reason)
admin.site.register(Operator)
admin.site.register(Status)
admin.site.register(Call)
