from django.http import HttpResponse


def index(request):
    return HttpResponse('I got it!')


def second_page(request):
    return HttpResponse('А это вторая страница')
