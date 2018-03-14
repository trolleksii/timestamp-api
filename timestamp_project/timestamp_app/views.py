from datetime import datetime

from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse


class IndexView(TemplateView):
    template_name = 'api_index.html'


class TimeStampView(View):

    def _parse_date_or_timestamp(self, date_string, DATE_FORMATS=['%B %d, %Y', ]):
        """
        Tries to convert string to a date, if the string is a timestamp or a
        natural date representation('123123', '213123.23' or 'March 15, 2018').
        Optionally you can pass an extended list of date formats DATE_FORMAT.
        Information about acceptable format strings can be found here:
        https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior
        Returns dictionary with timestamp and natural date representation, eg:
        {
            'unix': 123123,
            'natural': 'January 02, 1970'
        }
        If the string could not be converted - both fields will be None:
        {
            'unix': None,
            'natural': None
        }
        """
        timestamp = None
        natural_date = None
        # check if a date_string is timestamp
        try:
            natural_date = datetime.fromtimestamp(float(date_string)).strftime('%B %d, %Y')
            timestamp = date_string
        except OverflowError:
            # number is too big for a timestamp
            pass
        except ValueError:
            # not a timestamp
            for date_format in DATE_FORMATS:
                try:
                    timestamp = str(datetime.strptime(date_string, date_format).timestamp())
                    natural_date = date_string
                    break
                except ValueError:
                    continue
        return {'unix': timestamp, 'natural': natural_date}

    def get(self, request, *args, **kwargs):
        date_string = kwargs.get('date', '')
        data = self._parse_date_or_timestamp(date_string)
        return JsonResponse(data)
