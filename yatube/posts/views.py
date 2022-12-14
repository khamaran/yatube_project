from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Yatube'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube.',
    }
    return render(request, template, context) 

# Страница, на которой будут посты, отфильтрованные по группам.
def group_posts(request):
    template = 'posts/group_list.html'
    title = 'Yatube'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube.',
    }
    return render(request, template, context) 

