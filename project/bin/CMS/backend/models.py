from django.db import models


# Шаблоны body элемента
class BodyTemplate(models.Model):
    name = models.CharField(max_length=400)
    temp_body_id = models.CharField(max_length=500)
    text = models.TextField


# Шаблоны div элементов
class DivSTemplate(models.Model):
    name = models.CharField(max_length=400)
    temp_body_id = models.CharField(max_length=500)
    header = models.TextField
    text = models.TextField


# Шаблоны страниц
class HTMLTemplate(models.Model):
    name = models.CharField(max_length=400)
    use_name = models.CharField(max_length=500)
    header = models.TextField
    body_numbers = models.CharField(max_length=1000)


# Шаблоны созданых Body элементов
class BodyTemplateContent(models.Model):
    template = models.ForeignKey(BodyTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=400)
    temp_body_id = models.CharField(max_length=500)
    text = models.TextField


# Шаблоны созданых div элементов
class DivSTemplateContent(models.Model):
    template = models.ForeignKey(DivSTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=400)
    temp_body_id = models.CharField(max_length=500)
    header = models.TextField
    text = models.TextField
