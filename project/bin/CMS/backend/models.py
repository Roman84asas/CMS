from django.db import models


# Шаблоны body элемента
class BodyTemplate(models.Model):
    name = models.CharField(max_length=400)
    temp_body_id = models.CharField(max_length=500)
    text = models.TextField(null=True)


# Шаблоны div элементов
class DivSTemplate(models.Model):
    name = models.CharField(max_length=400)
    temp_body_id = models.CharField(max_length=500)
    header = models.TextField(null=True)
    text = models.TextField(null=True)


# Шаблоны страниц
class HTMLTemplate(models.Model):
    name = models.CharField(max_length=400)
    use_name = models.CharField(max_length=500)
    header = models.TextField(null=True)
    body_numbers = models.CharField(max_length=1000)


# Шаблоны созданых Body элементов
class BodyTemplateContent(models.Model):
    template = models.ForeignKey(BodyTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=400)
    temp_body_id = models.CharField(max_length=500)
    text = models.TextField(null=True)


# Шаблоны созданых div элементов
class DivSTemplateContent(models.Model):
    template = models.ForeignKey(DivSTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=400)
    temp_body_id = models.CharField(max_length=500)
    header = models.TextField(null=True)
    text = models.TextField(null=True)
