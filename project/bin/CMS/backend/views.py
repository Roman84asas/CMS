from django.shortcuts import render

# Загрузачная страница с выводом ссылок на редактор существующих страницы
from backend.forms import FormBody, FormDives
from backend.models import BodyTemplate


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
    if request.method == 'POST':
        name = request.POST.get('name')
        name_id = request.POST.get('name_id')
        all_body = request.POST.get('all_body')
        body_template = BodyTemplate(name=name, temp_body_id=name_id, text=all_body)
        body_template.save()
        form_body = FormBody()
        form_body.initial["name"] = name
        form_body.initial["name_id"] = name_id
        form_body.initial["all_body"] = all_body
        return render(request, 'bodys/create.html', {"form": form_body})
    else:
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
