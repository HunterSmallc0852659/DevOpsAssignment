import unittest
from Assignment2.app import flask_app  # Import the Flask app


def create_app():
    """
    Create and return a Flask application instance.
    """
    return flask_app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        """
        Set up the test client for the Flask app.
        """
        self.app = create_app()
        self.client = self.app.test_client()

    def test_invalid_request_method(self):
        """
        Test that the `/` route returns a 405 status code for invalid request methods.
        """
        # Attempt a POST request on `/`
        response = self.client.post('/')

        # Assert the response status code is 405 (Method Not Allowed)
        self.assertEqual(response.status_code, 405)

        # Optionally, check the response message (if applicable)
        self.assertIn("Method Not Allowed", response.data.decode())


if __name__ == "__main__":
    unittest.main()
