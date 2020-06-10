from django.http import HttpResponse
from django.shortcuts import render, redirect
from users import models

# Create your views here.

def skip(request):
    host = request.META['HTTP_HOST']
    short_link = "http://" + host + request.get_full_path()
    print(short_link)
    long_link = models.Link.objects.get(short_link = short_link).long_link
    print(long_link)

    return redirect(str(long_link))
    # return HttpResponse("ok")