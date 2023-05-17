from rest_framework import serializers 
from .models import de

class deSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = de 
        fields = '__all__' 
