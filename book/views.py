from django.shortcuts import render

from django.shortcuts import HttpResponse
from .models import Book
# Create your views here.
def book_list(request):
    b= Book.objects.all()
    return HttpResponse('Book List Here')

def book_details(request):
    ...

def book_update(request,pk):
    ...

#Class Based View [EXPLORE]
