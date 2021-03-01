from django.http import JsonResponse
from django.shortcuts import render

# Загрузачная страница с выводом ссылок на редактор существующих страницы
from backend.forms import FormBody, FormDives
from .models import BodyTemplate, DivSTemplate
from .services import return_all_object, return_body_object, return_dives_object, return_new_body, return_body_form, \
    create_body, delete_body


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
    # Возвращает все элементы из базы данных для виджета
    body, dives, htmles = return_all_object()

    if request.method == 'POST':
        name = request.POST.get('name')
        name_id = request.POST.get('name_id')
        all_body = request.POST.get('all_body')

        # Обновляет данные BODY секции
        return_new_body(elementid, name, name_id, all_body)

        # Возвращает форму для BODY секции
        form_body = return_body_form(name, name_id, all_body)

        return render(request, 'bodys/index.html',
                      {"form": form_body, 'bodys': body, 'dives': dives, 'htmles': htmles})
    else:
        # Возвращает данные BODY секции
        name, name_id, all_body = return_body_object(elementid)

        # Возвращает форму для BODY секции
        form_body = return_body_form(name, name_id, all_body)

        return render(request, 'bodys/index.html',
                      {"form": form_body, 'bodys': body, 'dives': dives, 'htmles': htmles})


def delete_body_id(request):
    data = {'msg': ''}
    id_delete = request.POST.get('id_delete')
    if not id_delete:
        return
    else:
        delete_body(id_delete)
        data['msg'] = id_delete + ' delete'
        return JsonResponse(data)


def create_bodys(request, elementid):
    # Возвращает все элементы из базы данных для виджета
    body, dives, htmles = return_all_object()

    if request.method == 'POST':
        name = request.POST.get('name')
        name_id = request.POST.get('name_id')
        all_body = request.POST.get('all_body')

        # Создает данные BODY секции
        create_body(name, name_id, all_body)

        # Возвращает форму для BODY секции
        form_body = return_body_form(name, name_id, all_body)

        return render(request, 'bodys/create.html',
                      {"form": form_body, 'bodys': body, 'dives': dives, 'htmles': htmles})
    else:
        # Возвращает данные BODY секции
        name, name_id, all_body = return_body_object(elementid)

        # Возвращает форму для BODY секции
        form_body = return_body_form(name, name_id, all_body)

        return render(request, 'bodys/create.html',
                      {"form": form_body, 'bodys': body, 'dives': dives, 'htmles': htmles})


# Див элементы и методы работы с ними
def index_dives(request, elementid):
    name, name_id, title_body, all_body = return_dives_object(elementid)
    # Возвращает все элементы из базы данных для виджета
    body, dives, htmles = return_all_object()
    # Возвращает форму для DIV секции
    form_dives = FormDives()
    form_dives.initial["name"] = name
    form_dives.initial["name_id"] = name_id
    form_dives.initial["title_body"] = title_body
    form_dives.initial["all_body"] = all_body
    return render(request, 'dives/index.html', {"form": form_dives, 'bodys': body, 'dives': dives, 'htmles': htmles})


def create_dives(request, elementid):
    name, name_id, title_body, all_body = return_dives_object(elementid)
    # Возвращает все элементы из базы данных для виджета
    body, dives, htmles = return_all_object()
    if request.method == 'POST':
        name = request.POST.get('name')
        name_id = request.POST.get('name_id')
        title_body = request.POST.get('title_body')
        all_body = request.POST.get('all_body')
        divs_template = DivSTemplate(name=name, temp_body_id=name_id, header=title_body, text=all_body)
        divs_template.save()
        # Возвращает форму для DIV секции
        form_dives = FormDives()
        form_dives.initial["name"] = name
        form_dives.initial["name_id"] = name_id
        form_dives.initial["title_body"] = title_body
        form_dives.initial["all_body"] = all_body
        return render(request, 'dives/create.html',
                      {"form": form_dives, 'bodys': body, 'dives': dives, 'htmles': htmles})
    else:
        # Возвращает форму для DIV секции
        form_dives = FormDives()
        form_dives.initial["name"] = name
        form_dives.initial["name_id"] = name_id
        form_dives.initial["title_body"] = title_body
        form_dives.initial["all_body"] = all_body
        return render(request, 'dives/create.html',
                      {"form": form_dives, 'bodys': body, 'dives': dives, 'htmles': htmles})
