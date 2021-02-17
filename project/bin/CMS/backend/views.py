from django.shortcuts import render


# Загрузачная страница с выводом ссылок на редактор существующих страницы
def index(request):
    return render(request, 'index.html')
