from .models import BodyTemplate, DivSTemplate, HTMLTemplate


def return_all_object():
    body = BodyTemplate.objects.all()
    dives = DivSTemplate.objects.all()
    htmles = HTMLTemplate.objects.all()
    return body, dives, htmles


def return_body_object(elementid):
    body = BodyTemplate.objects.get(id=elementid)
    return body.name, body.temp_body_id, body.text
