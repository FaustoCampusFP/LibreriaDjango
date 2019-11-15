from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    libros = Book.objects.all()
    return render(request, 'libreria.html', {'todo':libros})