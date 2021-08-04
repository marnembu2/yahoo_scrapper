from django.test import TestCase
from .models import Article
from django.utils.crypto import get_random_string
import datetime


class ArticleTestCase(TestCase):

    def test_object_creation(self):
        try:
            Article.objects.create(
                title='title test',
                description='description test',
                guid=get_random_string(length=32),
                guid_is_perma_link=True,
                link='https://google.com',
                pubDate=datetime.datetime.now()
            )
        except Exception:
            self.fail('System can not insert new Article into database')

    def test_objects_selecting_from_database(self):
        try:
            Article.objects.all()
        except Exception:
            self.fail('Can not get articles')

    def test_news_url(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)


