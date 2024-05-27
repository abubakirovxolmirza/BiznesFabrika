from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Auktsion, Buyum, Tasks, HistoryBalls, HistoryTasks, Balls
from .serializers import AuktsionSerializer, BuyumTaskssSerializer, TasksSerializer, HistoryBallsSerializer, HistoryTasksSerializer, BallsSerializer
# Create your views here.


class AuktsionCreateListView(ListCreateAPIView):
    queryset = Auktsion.objects.all()
    serializer_class = AuktsionSerializer
    

class BuyumCreateListView(ListCreateAPIView):
    queryset = Buyum.objects.all()
    serializer_class = BuyumTaskssSerializer
    
    
class TasksCreateListView(ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    
    
class HistoryBallsCreateListView(ListCreateAPIView):
    queryset = HistoryBalls.objects.all()
    serializer_class = HistoryBallsSerializer
    
    
class HistoryTasksCreateListView(ListCreateAPIView):
    queryset = HistoryTasks.objects.all()
    serializer_class = HistoryTasksSerializer
    
    
class BallsTasksCreateListView(ListCreateAPIView):
    queryset = Balls.objects.all()
    serializer_class = BallsSerializer
    
    

    

class AuktsionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Auktsion.objects.all()
    serializer_class = AuktsionSerializer
    
    
class BuyumDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Buyum.objects.all()
    serializer_class = BuyumTaskssSerializer
    
    
class TasksDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    
    
class HistoryBallsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HistoryBalls.objects.all()
    serializer_class = HistoryBallsSerializer
    
    
class HistoryTasksDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HistoryTasks.objects.all()
    serializer_class = HistoryTasksSerializer
    
    
class BallsTasksDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Balls.objects.all()
    serializer_class = BallsSerializer