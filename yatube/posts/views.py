from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template) 

# Страница, на которой будут посты, отфильтрованные по группам.
def group_posts(request, slug):
    return HttpResponse(f'На этой странице будут посты, отфильтрованные по группам {slug}.')

