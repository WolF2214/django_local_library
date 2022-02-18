from rest_framework import viewsets 
from .serializers import UserSerializer, MarkerSerializer
from .models import User, Marker

class UserViewSet(viewsets.ModelViewSet): 
    queryset = User.objects.all().order_by('first_name') 
    serializer_class = UserSerializer

class MarkerViewSet(viewsets.ModelViewSet): 
    queryset = Marker.objects.all().order_by() 
    serializer_class = MarkerSerializer

