from flask import url_for

from tests import BaseTestCase


class ViewsTestCase(BaseTestCase):
    def test_home_page(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue(b'Hello world!' in response.data)
