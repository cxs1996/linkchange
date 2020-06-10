import json

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from users import models


class link_change(View):

    global num
    num = 100000000

    def post(self, request):
        global num
        num = num + 1
        k = convert(num=num)
        j = "http://127.0.0.1:8000/skip/" + k + "/"
        global long_link
        json_dict = json.loads(request.body.decode())
        long_link = json_dict.get('long_link')
        # print(type(k))
        print(num)
        print(j)
        models.Link.objects.create(long_link=long_link, short_link = j)

        return HttpResponse(j)


def convert(num):

    # global all_chars
    all_chars = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'
    digits = []
    while num>0:
        digits.insert(0, all_chars[num % 62])
        num //= 62

    k = ''.join(digits)
    return k



