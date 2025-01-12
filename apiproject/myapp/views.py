
from django.shortcuts import get_object_or_404
from myapp.serializers import contactSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from myapp.models import contact

from rest_framework import status

class contactViewSet(viewsets.ViewSet):
   
    def list(self, request):
        queryset = contact.objects.all()
        serializer = contactSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = contact.objects.all()
        contact = get_object_or_404(queryset, pk=pk)
        serializer = contactSerializer(contact)
        return Response(serializer.data)
     
    def create(self,request):
        Serializer=contactSerializer(data=request.data)
    
        if Serializer.is_valid():
         Serializer.save()
    
         return Response(Serializer.data,status=status.HTTP_201_CREATED)
     
     
     
     
     
        def update(self,request,pk=None):
          contact=contact.object.get(pk=pk)
          Serializer=contactSerializer(contact,data=request.data)
        if Serializer.is_valid():
             Serializer.save()
    
        return Response(Serializer.data)
        return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     
     
          
        
        