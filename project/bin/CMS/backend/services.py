from .forms import FormBody
from .models import BodyTemplate, DivSTemplate, HTMLTemplate


def return_all_object():
    body = BodyTemplate.objects.all()
    dives = DivSTemplate.objects.all()
    htmles = HTMLTemplate.objects.all()
    return body, dives, htmles


def return_body_form(name, name_id, all_body):
    form_body = FormBody()
    form_body.initial["name"] = name
    form_body.initial["name_id"] = name_id
    form_body.initial["all_body"] = all_body
    return form_body


def create_body(name, name_id, all_body):
    body_template = BodyTemplate(name=name, temp_body_id=name_id, text=all_body)
    body_template.save()


def return_body_object(elementid):
    body = BodyTemplate.objects.get(id=elementid)
    return body.name, body.temp_body_id, body.text


def return_new_body(elementid, name, name_id, all_body):
    body = BodyTemplate.objects.get(id=elementid)
    body.name = name
    body.temp_body_id = name_id
    body.text = all_body
    body.save()


def return_dives_object(elementid):
    body = DivSTemplate.objects.get(id=elementid)
    return body.name, body.temp_body_id, body.header, body.text
