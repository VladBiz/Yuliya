from django.http import HttpResponse


def index(request):
    return HttpResponse("s")


def index2(request):
    return HttpResponse("s2")