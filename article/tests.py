from http.client import BAD_REQUEST

from django.test import TestCase
from django.urls import reverse

from article.models import Article


# Create your tests here.
class CommentTest(TestCase):
    def setUp(self):
        self.url = reverse('comments')
        author = "author"
        title = "title"
        body = "body"
        self.article = Article.objects.create(author=author, title=title, body=body)

    def test_create_comment(self):
        data = {
            "author": "author",
            "body": "body",
            "article_id": self.article.pk
        }
        res = self.client.post(self.url, data)
        self.assertEqual(res.status_code, 200)

    # def test_with_data_not_in_JSON_format(self):
    #     data = [
    #         "author",
    #         "body"
    #     ]
    #     res = self.client.post(self.url, data)
    #     self.assertEqual(res.status_code, BAD_REQUEST)

    def test_create_comment_without_article_id(self):
        data = {
            "author": "author",
            "body": "body",
        }
        res = self.client.post(self.url, data)
        self.assertEqual(res.status_code, BAD_REQUEST)

    def test_create_comment_with_str_article_id(self):
        data = {
            "author": "author",
            "body": "body",
            "article_id": "id"
        }
        res = self.client.post(self.url, data)
        self.assertEqual(res.status_code, BAD_REQUEST)

    def test_create_comment_with_nonexistent_article_id(self):
        data = {
            "author": "author",
            "body": "body",
            "article_id": 111
        }
        res = self.client.post(self.url, data)
        self.assertEqual(res.status_code, BAD_REQUEST)

    def test_create_comment_without_author(self):
        data = {
            "body": "body",
            "article_id": self.article.pk
        }
        res = self.client.post(self.url, data)
        self.assertEqual(res.status_code, BAD_REQUEST)

    def test_create_comment_with_int_author(self):
        data = {
            "author": 55,
            "body": "body",
            "article_id": self.article.pk
        }
        res = self.client.post(self.url, data)
        self.assertEqual(res.status_code, BAD_REQUEST)

    def test_create_comment_without_body(self):
        data = {
            "author": "author",
            "article_id": self.article.pk
        }
        res = self.client.post(self.url, data)
        self.assertEqual(res.status_code, BAD_REQUEST)

    def test_create_comment_with_int_body(self):
        data = {
            "author": "author",
            "body": 123,
            "article_id": self.article.pk
        }
        res = self.client.post(self.url, data)
        self.assertEqual(res.status_code, BAD_REQUEST)
