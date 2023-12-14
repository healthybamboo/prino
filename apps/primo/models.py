from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    memo = models.TextField(blank=True, null=True)
    end_at = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Job(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    shedule = models.CharField(max_length=255)
    result = models.TextField(blank=True, null=True)
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
    description = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.movie.title
