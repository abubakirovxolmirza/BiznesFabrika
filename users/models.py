from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from armiya.models import HistoryBalls, Tasks
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    STATUS_CHOICES = [
        ('Asked', 'Asked'),
        ('Expected', 'Expected'),
        ('Done', 'Done'),
    ]
    
    ROLES_CHOICES = [
        ('General', 'General'),
        ('Mayor', 'Mayor'),
        ('Captain', 'Captain'),
        ('Leytenant', 'Leytenant'),
        ('Serjant', 'Serjant'),
        ('Kursant', 'Kursant'),
        ('Saldat', 'Saldat'),

    ]
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    vab = models.ForeignKey(HistoryBalls, on_delete=models.CASCADE, blank=True, null=True)
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE, blank=True, null=True)
    reyting = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLES_CHOICES, blank=True, null=True)
    permission = models.CharField(max_length=70, blank=True, null=True)
    history_tasks = models.CharField(max_length=50, blank=True, null=True)
    history_balls = models.CharField(max_length=70, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
        
    def get_role(self)-> str:
        return self.role
    
    # def __str__(self):
    #     return self.tasks
    
    def get_user_id(self):
        return self.id
        
            