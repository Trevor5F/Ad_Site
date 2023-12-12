from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.author
