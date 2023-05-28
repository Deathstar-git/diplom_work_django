from django.http import HttpResponseNotFound
from django.shortcuts import render


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def main(request):
    return render(request, 'main/main.html', locals())