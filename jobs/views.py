from django.shortcuts import render

from .models import Job
from books.models import Book
from videos.models import Video


def home(request):
	jobs = Job.objects
	books = Book.objects
	videos = Video.objects
	return render(request, 'jobs/home.html', {'jobs':jobs, 'books':books, 'videos':videos})
