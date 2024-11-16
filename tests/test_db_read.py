import unittest
from pymongo import MongoClient

class TestDatabaseRead(unittest.TestCase):
    def setUp(self):
        """
        Set up a connection to the MongoDB instance and select a test database.
        """
        self.client = MongoClient("mongodb+srv://c0852659:zYAa2zCOPLhuHCJr@cluster0.j7lmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Replace with your connection URI
        self.db = self.client['shop_db']  # Reference the `shop_db` database
        self.collection = self.db['products']  # Reference the `products` collection
    def test_mongodb_connection(self):
        """
        Test that the MongoDB database is reachable using a ping operation.
        """
        result = self.client.admin.command('ping')  # Send a ping to the database
        self.assertIn('ok', result)  # Check the response contains 'ok'
        self.assertEqual(result['ok'], 1)  # Confirm the value of 'ok' is 1

    def tearDown(self):
        """
        Clean up the test database after the tests are run.
        """
        # Clean up the `products` collection only, to avoid dropping the entire database.
        self.collection.delete_many({})  # Remove all test documents from the collection

if __name__ == "__main__":
    unittest.main()
