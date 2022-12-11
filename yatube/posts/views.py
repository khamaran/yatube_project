from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница, на которой будут посты, отфильтрованные по группам.
def group_posts(request, slug):
    return HttpResponse(f'На этой странице будут посты, отфильтрованные по группам {slug}.')

