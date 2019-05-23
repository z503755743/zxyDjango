from django.shortcuts import render
from .models import Book
# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world!")

def detail(request):
	book_list = Book.objects.order_by('-pub_date')[:5]
	context = {'book_list': book_list}
	return render(request, 'lib/detail.html', context)