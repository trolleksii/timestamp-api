from django.test import SimpleTestCase
from django.urls import reverse

from timestamp_app.views import TimeStampView


class APIIndexViewTest(SimpleTestCase):

    def test_template(self):
        response = self.client.get(reverse('timestamp_app:index_view'))
        self.assertTemplateUsed(response, 'api_index.html')


class TimeStampViewTest(SimpleTestCase):
    # these dates are valid for EET timezone only
    TEST_TIMESTAMP = '987627600.0'
    TEST_NATURAL_DATE = 'April 19, 2001'
    TEST_ALTERNATIVE_DATE = '19-04-2001'
    TEST_DATE_FORMATS = ['%d-%m-%Y', ]

    def test_date_parser(self):
        result = TimeStampView()._parse_date_or_timestamp(self.TEST_NATURAL_DATE)
        self.assertEqual(result, {'unix': self.TEST_TIMESTAMP, 'natural': self.TEST_NATURAL_DATE})

    def test_date_parser_with_formats(self):
        result = TimeStampView()._parse_date_or_timestamp(self.TEST_ALTERNATIVE_DATE, DATE_FORMATS=self.TEST_DATE_FORMATS)
        self.assertEqual(result, {'unix': self.TEST_TIMESTAMP, 'natural': self.TEST_ALTERNATIVE_DATE})

    def test_view_with_timestamp(self):
        response = self.client.get(reverse('timestamp_app:timestamp_view', args=(self.TEST_TIMESTAMP,)))
        self.assertEqual(response.json(), {'unix': self.TEST_TIMESTAMP, 'natural': self.TEST_NATURAL_DATE})

    def test_huge_number(self):
        response = self.client.get(reverse('timestamp_app:timestamp_view', args=('111111111111111111111111111111111111111111',)))
        self.assertEqual(response.json(), {'unix': None, 'natural': None})

    def test_view_with_date(self):
        response = self.client.get(reverse('timestamp_app:timestamp_view', args=(self.TEST_NATURAL_DATE,)))
        self.assertEqual(response.json(), {'unix': self.TEST_TIMESTAMP, 'natural': self.TEST_NATURAL_DATE})

    def test_view_with_nonsense(self):
        response = self.client.get(reverse('timestamp_app:timestamp_view', args=('some nonsense string',)))
        self.assertEqual(response.json(), {'unix': None, 'natural': None})
