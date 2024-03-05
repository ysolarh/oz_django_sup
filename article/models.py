from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    body = models.TextField()


class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    @classmethod
    def create_one(cls, author: str, body: str, article_id: int) -> "Comment":
        return cls.objects.create(
            author=author,
            body=body,
            article_id=article_id,
        )
