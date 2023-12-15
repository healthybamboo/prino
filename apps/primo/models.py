from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField()
    memo = models.TextField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    is_active = models.BooleanField(default=True)
    status = models.CharField(
        max_length=20,
        choices=(
            ('pending', '保留中'),
            ('running', '実行中'),
            ('failed', '失敗'),
            ('completed', '完了'),
        ),
        default='pending',
    )
    image = models.URLField(blank=True, null=True)
    episode = models.CharField(max_length=100, blank=True, null=True)
    episode_title = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title or self.url
