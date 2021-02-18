from django.shortcuts import render


# Загрузачная страница с выводом ссылок на редактор существующих страницы
def index(request):
    return render(request, 'index.html')


def index_htmles(request):
    return render(request, 'htmles/index.html')


def index_bodys(request):
    return render(request, 'bodys/index.html')


def index_dives(request):
    return render(request, 'dives/index.html')
