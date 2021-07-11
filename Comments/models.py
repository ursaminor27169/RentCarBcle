from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, db_index=True, verbose_name='Заголовок', default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст комментария')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-create_date']
