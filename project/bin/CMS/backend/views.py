from django.shortcuts import render


# Загрузачная страница с выводом ссылок на редактор существующих страницы
def index(request):
    return render(request, 'index.html')


def index_htmles(request):
    return render(request, 'htmles/index.html')


def create_htmles(request):
    return render(request, 'htmles/create.html')


def index_bodys(request):
    return render(request, 'bodys/index.html')


def create_bodys(request):
    return render(request, 'bodys/create.html')


def index_dives(request):
    return render(request, 'dives/index.html')


def create_dives(request):
    return render(request, 'dives/create.html')
