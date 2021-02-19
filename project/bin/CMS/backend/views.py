from django.shortcuts import render


# Загрузачная страница с выводом ссылок на редактор существующих страницы
from backend.forms import FormBody, FormDives


def index(request):
    return render(request, 'index.html')


def index_htmles(request):
    return render(request, 'htmles/index.html')


def create_htmles(request):
    return render(request, 'htmles/create.html')


def index_bodys(request):
    form_body = FormBody()
    form_body.initial["name"] = 'Основной термидеск'
    form_body.initial["name_id"] = 'Описание идентификатора для привязки шаблона'
    form_body.initial["all_body"] = 'Content'
    return render(request, 'bodys/index.html', {"form": form_body})


def create_bodys(request):
    form_body = FormBody()
    form_body.initial["name"] = 'Основной термидеск'
    form_body.initial["name_id"] = 'Описание идентификатора для привязки шаблона'
    form_body.initial["all_body"] = 'Content'
    return render(request, 'bodys/create.html', {"form": form_body})


def index_dives(request):
    form_dives = FormDives()
    form_dives.initial["name"] = 'Основной термидеск'
    form_dives.initial["name_id"] = 'Описание идентификатора для привязки шаблона'
    form_dives.initial["title_body"] = 'Content title'
    form_dives.initial["all_body"] = 'Content all'
    return render(request, 'dives/index.html', {"form": form_dives})


def create_dives(request):
    form_dives = FormDives()
    form_dives.initial["name"] = 'Основной термидеск'
    form_dives.initial["name_id"] = 'Описание идентификатора для привязки шаблона'
    form_dives.initial["title_body"] = 'Content title'
    form_dives.initial["all_body"] = 'Content all'
    return render(request, 'dives/create.html', {"form": form_dives})
