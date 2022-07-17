from django.urls import reverse

from model_bakery import baker

from rest_framework import status

from rest_framework.test import APITestCase

from .models import CandleStick


class CandleStickViewSetTestCase(APITestCase):

    def setUp(self):
        self.candleStick = baker.make(
            CandleStick,
            dolar='1',
            euro='0.9',
            jpy='105.2',
            real='5',
            period='2022-07-17 18:22',
        )

        self.dolar = '1'
        self.euro = '0.9'
        self.jpy = '105.2'
        self.real = '5'
        self.period = '2022-07-17 18:22'

    def test_view_search_currency_by_real(self):
        """
        tests search currency by Real.
        """
        url = 'http://127.0.0.1:8000/' \
              'candle/consulta/real/2022-07-17/2022-07-17'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_search_currency_by_euro(self):
        """
        tests search currency by Euro.
        """
        url = 'http://127.0.0.1:8000/' \
              'candle/consulta/euro/2022-07-17/2022-07-17'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_search_currency_by_joy(self):
        """
        tests search currency by jpy.
        """
        url = 'http://127.0.0.1:8000/candle/consulta/jpy/2022-07-15/2022-07-16'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serializer_invalid_search(self):
        """
        Test test invalid search.
        """

        url = 'http://127.0.0.1:8000/' \
              'candle/consulta/peso/2022-07-15/2022-07-16'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
