from django.test import TestCase
import feedparser
from django.conf import settings
import urllib.request


class UrlTesting(TestCase):

    def test_settings(self):
        strings = settings.SCRAPPING_KEYWORDS
        if len(strings) == 0:
            self.fail("Configurations are wrong, no KEY STRINGS")

    def test_url_availability(self):
        for string in settings.SCRAPPING_KEYWORDS:
            url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=' + string + '&region=US&lang=en-US'
            try:
                fp = urllib.request.urlopen(url)
                fp.read().decode("utf8")
                fp.close()
            except Exception:
                self.fail('Given url is not working')

    def test_data_on_url(self):
        for string in settings.SCRAPPING_KEYWORDS:
            url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=' + string + '&region=US&lang=en-US'
            data = feedparser.parse(url)

            if len(data.entries) == 0:
                self.fail('No data on the link: ' + url + ' , data: ' + str(data))

    def test_data_structure(self):
        data = feedparser.parse('https://feeds.finance.yahoo.com/rss/2.0/headline?s=' + settings.SCRAPPING_KEYWORDS[
            0] + '&region=US&lang=en-US')

        for item in data.entries:
            try:
                if item.title and item.summary and item.id and item.guidislink and item.link and item.published:
                    pass
            except Exception:
                self.fail('Object witch is parsing is not as expected, scrapper is not working. Object: ' + str(item))


