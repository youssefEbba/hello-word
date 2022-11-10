
from django.http import HttpResponse


def homePegeView(request):
    return HttpResponse('Hello, Word')
