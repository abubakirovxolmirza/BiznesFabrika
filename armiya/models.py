from django.db import models
# from users.models import CustomUser
# Create your models here.
    
    
class Tasks(models.Model):
    STATUS_CHOICES = [
        ('Asked', 'Asked'),
        ('Expected', 'Expected'),
        ('Done', 'Done'),
    ]
    name = models.CharField(max_length=250)
    definition = models.CharField(max_length=250)
    ball = models.IntegerField()
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    users = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='armiya_tasks')
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    

class HistoryTasks(models.Model):
    tasks_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    ball = models.IntegerField()
    definition = models.CharField(max_length=250)
    
class Balls(models.Model):
    STATUS_CHOICES = [
        ('Asked', 'Asked'),
        ('Expected', 'Expected'),
        ('Done', 'Done'),
    ]
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)
    ball = models.IntegerField()
    definition = models.CharField(max_length=250)
    tasks_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    
    
    
class HistoryBalls(models.Model):
    STATUS_CHOICES = [
        ('Asked', 'Asked'),
        ('Expected', 'Expected'),
        ('Done', 'Done'),
    ]
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)
    ball = models.IntegerField()
    definition = models.CharField(max_length=250)
    balls_id = models.ForeignKey(Balls, on_delete=models.CASCADE)


    
    
class Buyum(models.Model):
    name = models.CharField(max_length=250)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ekb_name = models.CharField(max_length=200)
    ekb = models.IntegerField()
    boshlangich_narx = models.CharField(max_length=250)
    
    
class Auktsion(models.Model):
    name = models.CharField(max_length=250)
    kuni = models.DateField()
    yutganlar = models.CharField(max_length=100)
    buyumlar = models.ForeignKey(Buyum, on_delete=models.CASCADE)

