import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.connection import get_db_connection

class TestModels(unittest.TestCase):

    def setUp(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        cursor.execute("DELETE FROM articles")
        connection.commit()
        connection.close()
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertIsNotNone(author.id)
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):

        magazine = Magazine("Tech Weekly", "Technology")
        self.assertIsNotNone(magazine.id)
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

        # magazine = Magazine(1, "Tech Weekly")
        # self.assertEqual(magazine.name, "Tech Weekly")

if __name__ == "__main__":
    unittest.main()
