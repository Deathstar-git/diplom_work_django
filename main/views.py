from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.db.models import Q
from main.models import Fridge, MobilePhone, Multicooker


def search(request):
    results = []
    q = request.GET.get('query').capitalize()
    if q:
        fridges = Fridge.objects.filter(Q(title__icontains=q))[:5]
        mobile_phones = MobilePhone.objects.filter(Q(title__icontains=q))[:5]
        multicookers = Multicooker.objects.filter(Q(title__icontains=q))[:5]
        results.extend([{'name': fridge.title, 'url': fridge.get_absolute_url()} for fridge in fridges])
        results.extend([{'name': mobile_phone.title, 'url': mobile_phone.get_absolute_url()} for mobile_phone in mobile_phones])
        results.extend([{'name': cooker.title, 'url': cooker.get_absolute_url()} for cooker in multicookers])

    return JsonResponse(results, safe=False)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Not Found</h1>')


def main(request):
    fridges = Fridge.objects.all()
    n_col = int(fridges.count() / 6)
    title = 'Главная страница'
    return render(request, 'main/main.html', locals())


def fridge(request, _id):
    fridge = Fridge.objects.get(id=_id)
    title = fridge.title
    return render(request, 'fridge/fridge.html', locals())


def mobile_phone(request, _id):
    phone = MobilePhone.objects.get(id=_id)
    title = phone.title
    return render(request, 'mobile_phone/mobile_phone.html', locals())


def multicooker(request, _id):
    multicooker = Multicooker.objects.get(id=_id)
    title = multicooker.title
    return render(request, 'multicooker/multicooker.html', locals())


def mobile_phones(request):
    mobile_phones = MobilePhone.objects.all()
    n_col = int(mobile_phones.count() / 6)
    title = 'Мобильные телефоны'
    return render(request, 'mobile_phone/mobile_phones.html', locals())


def multicookers(request):
    multicookers = Multicooker.objects.all()
    n_col = int(multicookers.count() / 6)
    title = 'Мультиварки'
    return render(request, 'multicooker/multicookers.html', locals())