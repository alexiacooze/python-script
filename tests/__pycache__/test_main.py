import unittest
from flask import Flask
from main import app  # Adjust the import if your Flask app is in a different file

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_script(self):
        response = self.app.post('/execute', json={
            'script': 'def main(): return {"message": "Hello, world!"}'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, world!"})

    def test_no_json_payload(self):
        response = self.app.post('/execute')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Request must be in JSON format", response.json["error"])

    def test_no_script_provided(self):
        response = self.app.post('/execute', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("No script provided", response.json["error"])

    def test_non_string_script(self):
        response = self.app.post('/execute', json={'script': 12345})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Script must be a string", response.json["error"])

    def test_disallowed_keyword(self):
        response = self.app.post('/execute', json={'script': 'import os'})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Script contains disallowed keywords", response.json["error"])

    def test_missing_main_function(self):
        response = self.app.post('/execute', json={'script': 'def test(): pass'})
        self.assertEqual(response.status_code, 400)
        self.assertIn("The script must define a callable 'main' function", response.json["error"])

    def test_non_json_serializable_return(self):
        response = self.app.post('/execute', json={'script': 'def main(): return set([1, 2, 3])'})
        self.assertEqual(response.status_code, 400)
        self.assertIn("The 'main' function must return a JSON serializable dictionary", response.json["error"])

if __name__ == '__main__':
    unittest.main()
