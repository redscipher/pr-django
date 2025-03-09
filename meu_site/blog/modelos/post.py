from django.db import models
#importacoes
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, 'rascunho'),
    (1, 'publicar')
)

class Post(models.Model):
    
    #propriedades
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    dta_atualizacao = models.DateTimeField(auto_now=True)
    conteudo = models.TextField()
    dta_criacao = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    #sobreescreve classe do django
    class Meta:
        #propriedade da classe 'Meta' do django: "-" indica que eh decrescente
        ordering = ['-dta_criacao']
        
    def __str__(self):
        return self.titulo