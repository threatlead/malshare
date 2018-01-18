import requests
from datetime import datetime
from collections import namedtuple
import re


class Malshare:
    """
    Malshare : Ingest malware data
    """
    data = namedtuple('Malshare', ['hash', 'date'])
    base_url = 'http://malshare.com'

    @classmethod
    def _get_dates(cls):
        url = '{0}/daily'.format(cls.base_url)
        response = requests.get(url=url)
        if response.status_code != requests.codes.ok:
            raise Exception('Unable to connect to Malshare.com')
        # --
        dates = []
        for match in re.finditer('</td><td><a href="([\d\-]{8,10})/">', response.content.decode('ascii')):
            dates.append(datetime.strptime(match.groups()[0], '%Y-%m-%d'))
        return dates

    @classmethod
    def _get_sha256_data(cls, date):
        url = '{0}/daily/{1}/malshare_fileList.{1}.sha256.txt'.format(cls.base_url, date.strftime('%Y-%m-%d'))
        response = requests.get(url=url)
        if response.status_code != requests.codes.ok:
            raise Exception('Unable to connect to Malshare.com')
        # --
        malshare = []
        for sha256 in response.content.splitlines():
            malshare.append(cls.data(hash=sha256.decode('ascii'), date=date))
        return malshare

    @classmethod
    def get_all_dates(cls):
        date_set = cls._get_dates()
        malshare = []
        for date in date_set:
            malshare += cls._get_sha256_data(date=date)
        return malshare

    @classmethod
    def get_latest(cls):
        max_date = max(cls._get_dates())
        return cls._get_sha256_data(date=max_date)

