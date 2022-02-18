from rest_framework import serializers
from .models import User, Marker

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

class MarkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marker
        fields = ('owner', 'model', 'brand', 'fps', 'rol', 'upload_date')