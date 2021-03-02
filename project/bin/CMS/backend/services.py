from .forms import FormBody, FormDives
from .models import BodyTemplate, DivSTemplate, HTMLTemplate


def return_all_object():
    body = BodyTemplate.objects.all()
    dives = DivSTemplate.objects.all()
    htmles = HTMLTemplate.objects.all()
    return body, dives, htmles


def return_all_html():
    htmle = HTMLTemplate.objects.all()
    return htmle


def html_content(elementid):
    html_template = HTMLTemplate.objects.get(id=elementid)
    return html_template


def create_new_html(name, use_name, body_numbers):
    html_template = HTMLTemplate(name=name, use_name=use_name, header='New', body_numbers=body_numbers)
    html_template.save()
    return html_template


def update_html(id_el, name, use_name, body_numbers):
    html_template = HTMLTemplate.objects.get(id=id_el)
    html_template.name = name
    html_template.use_name = use_name
    html_template.header = 'Update'
    html_template.body_numbers = body_numbers
    html_template.save()


def delete_html(id_html):
    html_template = HTMLTemplate.objects.get(id=id_html)
    html_template.delete()


def add_div(get_data):
    body = DivSTemplate.objects.get(id=get_data)
    return body


def add_header(get_data):
    body = BodyTemplate.objects.get(id=get_data)
    return body


def return_body_form(name, name_id, all_body):
    form_body = FormBody()
    form_body.initial["name"] = name
    form_body.initial["name_id"] = name_id
    form_body.initial["all_body"] = all_body
    return form_body


def create_body(name, name_id, all_body):
    body_template = BodyTemplate(name=name, temp_body_id=name_id, text=all_body)
    body_template.save()


def delete_body(id):
    body_template = BodyTemplate.objects.get(id=id)
    body_template.delete()


# Функции секции Div
def return_body_object(elementid):
    body = BodyTemplate.objects.get(id=elementid)
    return body.name, body.temp_body_id, body.text


def return_new_body(elementid, name, name_id, all_body):
    body = BodyTemplate.objects.get(id=elementid)
    body.name = name
    body.temp_body_id = name_id
    body.text = all_body
    body.save()


def create_div(name, name_id, title_body, all_body):
    divs_template = DivSTemplate(name=name, temp_body_id=name_id, header=title_body, text=all_body)
    divs_template.save()


def return_dives_object(elementid):
    body = DivSTemplate.objects.get(id=elementid)
    return body.name, body.temp_body_id, body.header, body.text


def add_dives(get_data):
    div = DivSTemplate.objects.get(id=get_data)
    return div


def return_div_form(name, name_id, title_body, all_body):
    form_dives = FormDives()
    form_dives.initial["name"] = name
    form_dives.initial["name_id"] = name_id
    form_dives.initial["title_body"] = title_body
    form_dives.initial["all_body"] = all_body
    return form_dives


def return_new_div(elementid, name, name_id, title_body, all_body):
    div = DivSTemplate.objects.get(id=elementid)
    div.name = name
    div.temp_body_id = name_id
    div.header = title_body
    div.text = all_body
    div.save()


def delete_div(id):
    div_template = DivSTemplate.objects.get(id=id)
    div_template.delete()
