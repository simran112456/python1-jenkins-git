from unittest import TestCase

from mypage2 import app
import json
class ProductTest(TestCase):
    def test_welcome(self):
        with app.test_client() as c:
            resp = c.get('/api/products')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), [{

            }])

















