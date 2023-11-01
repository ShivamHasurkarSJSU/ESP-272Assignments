import unittest
from app import app
from flask_testing import TestCase

class CreateServiceTest(TestCase):

    def create_app(self):
        return app

    def test_root_endpoint(self):
        response = self.client.get('/create')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
