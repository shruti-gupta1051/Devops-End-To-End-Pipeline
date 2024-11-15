import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.client.testing = True
        print("Test client setup complete.")

    def test_index_page(self):
        print("Running test: Index Page")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'GFG Snake Game Updated', response.data)
        print("Index page test passed.")

    def test_static_files(self):
        print("Running test: Static Files")
        response = self.client.get('/static/game.js')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'const canvas', response.data)
        print("Static files test passed.")

if __name__ == '__main__':
    unittest.main()
