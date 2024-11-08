from rest_framework import generics
from .models import Book
from .serializers import Bookserializers

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Book.objects.all()
    serializer_class = Bookserializers