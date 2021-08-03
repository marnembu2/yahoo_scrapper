from celery import shared_task
from get_news.parser import parse


@shared_task
def start_scrapper():
    return parse()


