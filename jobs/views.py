from django.shortcuts import render

from .models import Job, UrlHit, HitCount
from books.models import Book
from videos.models import Video


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def hit_count(request):
    if not request.session.session_key:
        request.session.save()
    s_key = request.session.session_key
    ip = get_client_ip(request)
    url, url_created = UrlHit.objects.get_or_create(url=request.path)

    if url_created:
        track, created = HitCount.objects.get_or_create(url_hit=url, ip=ip, session=s_key)
        if created:
            url.increase()
            request.session[ip] = ip
            request.session[request.path] = request.path
    else:
        if ip and request.path not in request.session:
            track, created = HitCount.objects.get_or_create(url_hit=url, ip=ip, session=s_key)
            if created:
                url.increase()
                request.session[ip] = ip
                request.session[request.path] = request.path
    return url.hits


def home(request):
	home_active = True
	hits = hit_count(request)
	jobs = Job.objects
	books = Book.objects
	videos = Video.objects
	return render(request, 'jobs/home.html', {'home_active':home_active, 'hits':hits, 'jobs':jobs, 'books':books, 'videos':videos})
