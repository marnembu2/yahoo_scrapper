import feedparser
import dateutil.parser
from serve_news.models import Article


def parse():

    params = ['AAPL', 'TWTR', 'GC=F(GOLD)', 'INTC']

    ids = list(Article.objects.all().values_list('guid', flat=True))

    for string in params:

        data = feedparser.parse('https://feeds.finance.yahoo.com/rss/2.0/headline?s=' + string + '&region=US&lang=en-US')

        for item in data.entries:

            if item.id not in ids:

                Article.objects.create(
                    title=item.title,
                    description=item.summary,
                    guid=item.id,
                    guid_is_perma_link=item.guidislink,
                    link= item.link,
                    pubDate=dateutil.parser.parse(item.published)
                )

    return ids


