from django.contrib import admin
#from .models import Group
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author') #отображение полей в админке
    search_fields = ('text',) # поиск по тексту
    #list_filter = ('pub_date') # фильтр по дате
    empty_value_display='-пусто'

'''class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description') #отображение полей в админке'''


admin.site.register(Post,PostAdmin)
