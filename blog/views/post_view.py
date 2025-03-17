import asyncio
import time
from django.views import generic
from django.http import HttpResponse, JsonResponse
import httpx
#from django.shortcuts import render

#importa post 
from blog.modelos import Post

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=0).order_by('-dta_criacao')
    template_name = "index.html"
    
class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
    
class ClsExibeBemVindo(generic.TemplateView):
    template_name = 'bem_vindo.html'
    
    def api(request):
        time.sleep(1)
        payload = {'message': 'Ola Mundo requisitivo!'}
        
        if 'task_id' in request.GET:
            payload['task_id'] = request.GET['task_id']
        
        return JsonResponse(payload)
        
    async def http_call_async():
        for num in range(1, 6):
            await asyncio.sleep(1)
            print(num)
        async with httpx.AsyncClient() as client:
            r = await client.get('https://httpbin.org')
            print(r)
            
    async def async_views(request):
        loop = asyncio.get_event_loop()
        loop.create_task(ClsExibeBemVindo.http_call_async())
        return HttpResponse('Chamada nao bloqueante')
    
    #def bemvindo(request):
     #   return render(request, 'bem_vindo.html')