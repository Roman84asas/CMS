from .models import BodyTemplate, DivSTemplate, HTMLTemplate


def return_all_object():
    body = BodyTemplate.objects.all()
    dives = DivSTemplate.objects.all()
    htmles = HTMLTemplate.objects.all()
    return body, dives, htmles


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
