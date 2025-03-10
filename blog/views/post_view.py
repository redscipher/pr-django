from django.views import generic

#importa post 
from blog.modelos import Post

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=0).order_by('-dta_criacao')
    template_name = "index.html"
    
class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"