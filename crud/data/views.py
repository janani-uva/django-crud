from rest_framework import generics
from .models import student
from .serializers import studentserializers

class studentListCreate(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializers
    
class studentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializers  

