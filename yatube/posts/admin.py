from django.contrib import admin
from .models import Post
from .models import Group

class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author','group') 
    # Позволит изменять поле group в любом посте
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',) 
    empty_value_display = '-пусто-' 

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)  

class GroupAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'slug', 'description') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title',) 
    empty_value_display = '-пусто-'

admin.site.register(Group, GroupAdmin)