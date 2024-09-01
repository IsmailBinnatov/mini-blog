from django.db import models


class Post(models.Model):
    ''' Данные о посте '''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Автор', max_length=100)
    created_at = models.DateField('Дата публикации', auto_now_add=True)
    img = models.ImageField('Изображение', upload_to='image/%Y', null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comment(models.Model):
    ''' Данные о комментарии '''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.name} - {self.post}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'