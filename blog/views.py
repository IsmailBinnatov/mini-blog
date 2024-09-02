from django.shortcuts import redirect, render
from django.views.generic.base import View
from blog.models import Post, Like
from blog.form import Comments


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


class AddComments(View):
    ''' Добавление комментариев '''

    def post(self, request, pk):
        form = Comments(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # настоящий ip-адрес
    else:
        ip = request.META.get('REMOTE_ADDR')  # удалённый ip-адрес
    return ip


class AddLike(View):
    ''' Добавление лайков '''
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Like.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Like()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')
        
        
class DisLike(View):
    ''' Удаление лайков '''
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Like.objects.get(ip=ip_client)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')