from django.contrib import admin
from .models import Auktsion, Buyum, HistoryBalls, Tasks, Balls
# Register your models here.
admin.site.register(Auktsion)
admin.site.register(Buyum)
admin.site.register(HistoryBalls)
# admin.site.register(HistoryTasks)
admin.site.register(Tasks)
admin.site.register(Balls)
# admin.site.register(Htasks)