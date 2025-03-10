from django.contrib import admin
from .modelos import Post

class PostAdmin(admin.ModelAdmin):
    #os campos precisam ser em ingles pois o django vem configurado com os nomes em ingles
    list_display = ('titulo', 'slug', 'status', 'dta_criacao')
    list_filter = ('status',)       #a virgula no final indica que eh um campo "tuple"
    search_fields = ['titulo', 'conteudo']
    prepopulated_fields = {'slug': ('titulo',)}     #virgula on final novamente: tuple

# Register your models here.
admin.site.register(Post, PostAdmin)