from django.shortcuts import render
from django.views.generic.base import View
from blog.models import Post


class PostView(View):
    ''' Вывод записей '''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'posts': posts})
    
    
class PostDetail(View):
    ''' Отдельная страница записи '''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/post.html', {'post': post})