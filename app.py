from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")


    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()


    '''
        The following is just for testing purposes, 
        you can modify it to meet the requirements of your implmentation.
    '''

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))

    conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

    

if __name__ == "__main__":
    main()


from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")


    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()


    '''
        The following is just for testing purposes, 
        you can modify it to meet the requirements of your implmentation.
    '''

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))

    conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        # Create a Magazine object without saving it to the database
        mag = Magazine(magazine["name"], magazine["category"], id=magazine["id"])
        print(mag)

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

    

if __name__ == "__main__":
    main()


# from database.setup import create_tables
# from database.connection import get_db_connection
# from models.article import Article
# from models.author import Author
# from models.magazine import Magazine

# class LibraryDB:
#     def __init__(self):
#         create_tables()

#     def add_author(self, name):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
#         author_id = cursor.lastrowid
#         conn.commit()
#         conn.close()
#         return author_id

#     def add_magazine(self, name, category):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
#         magazine_id = cursor.lastrowid
#         conn.commit()
#         conn.close()
#         return magazine_id

#     def add_article(self, title, content, author_id, magazine_id):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
#                        (title, content, author_id, magazine_id))
#         conn.commit()
#         conn.close()

#     def get_all_authors(self):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM authors')
#         authors = cursor.fetchall()
#         conn.close()
#         return authors

#     def get_all_magazines(self):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM magazines')
#         magazines = cursor.fetchall()
#         conn.close()
#         return magazines

#     def get_all_articles(self):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM articles')
#         articles = cursor.fetchall()
#         conn.close()
#         return articles

#     def close(self):
#         pass  # No persistent connection to close in this context

# def main():
#     db = LibraryDB()

#     while True:
#         print("\n1. Add new author")
#         print("2. Add new magazine")
#         print("3. Add new article")
#         # print("4. Get all authors")
#         # print("5. Get all magazines")
#         # print("6. Get all articles")
#         print("4. Quit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             name = input("Enter author's name: ")
#             author_id = db.add_author(name)
#             print(f"Author added with ID: {author_id}")
#         elif choice == "2":
#             name = input("Enter magazine name: ")
#             category = input("Enter magazine category: ")
#             magazine_id = db.add_magazine(name, category)
#             print(f"Magazine added with ID: {magazine_id}")
#         elif choice == "3":
#             title = input("Enter article title: ")
#             content = input("Enter article content: ")
#             author_id = int(input("Enter author ID: "))
#             magazine_id = int(input("Enter magazine ID: "))
#             db.add_article(title, content, author_id, magazine_id)
#             print("Article added successfully.")
#         # elif choice == "4":
#         #     authors = db.get_all_authors()
#         #     for author in authors:
#         #         print(Author(author["id"], author["name"]))
#         # elif choice == "5":
#         #     magazines = db.get_all_magazines()
#         #     for magazine in magazines:
#         #         mag = Magazine(magazine["name"], magazine["category"], id=magazine["id"])
#         #         print(mag)
#         # elif choice == "6":
#         #     articles = db.get_all_articles()
#         #     for article in articles:
#         #         print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))
#         elif choice == "4":
#             db.close()
#             break
#         else:
#             print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()