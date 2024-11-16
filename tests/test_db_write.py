import unittest
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient("mongodb+srv://c0852659:zYAa2zCOPLhuHCJr@cluster0.j7lmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Replace with your connection URI
        self.db = self.client['shop_db']  # Reference the `shop_db` database
        self.collection = self.db['products']  # Reference the `products` collection

    def test_insert_document(self):
        """
        Test inserting a document into MongoDB and verify its presence.
        """
        # Insert a test document
        doc = {"name": "Test User", "email": "test@example.com"}
        result = self.collection.insert_one(doc)

        # Check that an ID was returned for the inserted document
        self.assertIsNotNone(result.inserted_id)

        # Verify the inserted document
        inserted_doc = self.collection.find_one({"_id": result.inserted_id})
        self.assertIsNotNone(inserted_doc)
        self.assertEqual(inserted_doc['name'], "Test User")
        self.assertEqual(inserted_doc['email'], "test@example.com")

    def tearDown(self):
        """
        Clean up the test collection after tests.
        """
        self.collection.delete_many({})  # Remove all documents from the test collection

    if __name__ == "__main__":
        unittest.main()
