from rest_framework import serializers
from myapp.models import contact

class contactSerializer(serializers.ModelSerializer):
      
       class Meta:
        model = contact
        fields =['email', 'title', 'name']