from django.shortcuts import render

# Загрузачная страница с выводом ссылок на редактор существующих страницы
from backend.forms import FormBody, FormDives
from .models import BodyTemplate, DivSTemplate
from .services import return_all_object, return_body_object


def index(request):
    return render(request, 'index.html')


# Html элементы и методы работы с ними
def index_htmles(request):
    body, dives, htmles = return_all_object()
    return render(request, 'htmles/index.html', {'bodys': body, 'dives': dives, 'htmles': htmles})


def create_htmles(request):
    body, dives, htmles = return_all_object()
    return render(request, 'htmles/create.html', {'bodys': body, 'dives': dives, 'htmles': htmles})


# Боди элементы и методы работы с ними
def index_bodys(request, elementid):
    name, name_id, all_body = return_body_object(elementid)
    body, dives, htmles = return_all_object()
    form_body = FormBody()
    form_body.initial["name"] = name
    form_body.initial["name_id"] = name_id
    form_body.initial["all_body"] = all_body
    return render(request, 'bodys/index.html', {"form": form_body, 'bodys': body, 'dives': dives, 'htmles': htmles})


def create_bodys(request, elementid):
    body, dives, htmles = return_all_object()
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
        return render(request, 'bodys/create.html',
                      {"form": form_body, 'bodys': body, 'dives': dives, 'htmles': htmles})
    else:
        name, name_id, all_body = return_body_object(elementid)
        form_body = FormBody()
        form_body.initial["name"] = name
        form_body.initial["name_id"] = name_id
        form_body.initial["all_body"] = all_body
        return render(request, 'bodys/create.html',
                      {"form": form_body, 'bodys': body, 'dives': dives, 'htmles': htmles})


# Див элементы и методы работы с ними
def index_dives(request, elementid):
    body, dives, htmles = return_all_object()
    form_dives = FormDives()
    form_dives.initial["name"] = 'Основной термидеск'
    form_dives.initial["name_id"] = 'Описание идентификатора для привязки шаблона'
    form_dives.initial["title_body"] = 'Content title'
    form_dives.initial["all_body"] = 'Content all'
    return render(request, 'dives/index.html', {"form": form_dives, 'bodys': body, 'dives': dives, 'htmles': htmles})


def create_dives(request, elementid):
    body, dives, htmles = return_all_object()
    if request.method == 'POST':
        name = request.POST.get('name')
        name_id = request.POST.get('name_id')
        title_body = request.POST.get('title_body')
        all_body = request.POST.get('all_body')
        divs_template = DivSTemplate(name=name, temp_body_id=name_id, header=title_body, text=all_body)
        divs_template.save()
        form_dives = FormDives()
        form_dives.initial["name"] = name
        form_dives.initial["name_id"] = name_id
        form_dives.initial["title_body"] = title_body
        form_dives.initial["all_body"] = all_body
        return render(request, 'dives/create.html',
                      {"form": form_dives, 'bodys': body, 'dives': dives, 'htmles': htmles})
    else:
        form_dives = FormDives()
        form_dives.initial["name"] = 'Основной термидеск'
        form_dives.initial["name_id"] = 'Описание идентификатора для привязки шаблона'
        form_dives.initial["title_body"] = 'Content title'
        form_dives.initial["all_body"] = 'Content all'
        return render(request, 'dives/create.html',
                      {"form": form_dives, 'bodys': body, 'dives': dives, 'htmles': htmles})
