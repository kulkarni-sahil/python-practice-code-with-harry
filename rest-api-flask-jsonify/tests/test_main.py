import json
import unittest

from rest_api_flask_jsonify.main import app


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.client = app.test_client()

    def tearDown(self) -> None:
        self.client = None

    def test_something(self):
        response = self.client.get('/')
        self.assertEqual(response.data.decode(), "Hello World")

    def test_something_2(self):
        response = self.client.get('/armstrong/153')
        expected = {
            'Armstrong': True,
            'DigitRaisedToOrder': [27, 125, 1],
            'Number': 153
        }
        self.assertEqual(json.loads(response.data.decode()), expected)


if __name__ == '__main__':
    unittest.main()
