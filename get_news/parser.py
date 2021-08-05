import feedparser
import dateutil.parser
from django.conf import settings
from celery import shared_task
from serve_news.models import Article
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def create_article(title, description, id, guid_is_perma_link, link, pubDate, type):
    """
    Function for creating Article object
    :param title:
    :param description:
    :param id:
    :param guid_is_perma_link:
    :param link:
    :param pubDate:
    :return:
    """
    Article.objects.create(
        title=title,
        description=description,
        guid=id,
        guid_is_perma_link=guid_is_perma_link,
        link=link,
        pubDate=pubDate,
        type=type
    )


def get_data_from_link(param):
    """
    Function for getting data from URL with given PARAM
    :param param:
    :return:
    """
    return feedparser.parse('https://feeds.finance.yahoo.com/rss/2.0/headline?s=' + param + '&region=US&lang=en-US')


def get_existing_article_ids():
    """
    Function for getting ids from database for comparing
    :return:
    """
    return list(Article.objects.all().values_list('guid', flat=True))
    # we can use Redis for cashing if we expect large number of ids


@shared_task()
def parse():
    """
    Function for scrapping data from URL
    :return:
    """
    num_of_inserted = 0

    for string in settings.SCRAPPING_KEYWORDS:

        data = get_data_from_link(string)

        for item in data.entries:
            if item.id not in get_existing_article_ids():
                create_article(
                    item.title,
                    item.summary,
                    item.id,
                    item.guidislink,
                    item.link,
                    dateutil.parser.parse(item.published),
                    string
                )

                num_of_inserted += 1

    return 'Total new articles inserted: ' + str(num_of_inserted)


# left if there is a need to run from code
def parse_scheduled():
    """
    Function for creating Schedule Job, if there is a need to call it from code
    :return:
    """
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.MINUTES)

    PeriodicTask.objects.create(
        interval=schedule,
        name='Run scrapper scheduling',
        task='yahoo_scrapper.tasks.start_scrapper')

