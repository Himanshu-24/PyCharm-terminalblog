# import pymongo
#
# uri = "mongodb://127.0.0.1:27017"  #universal resource identifier
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']
#
# #students = collection.find({})
# students = [student['age'] for student in collection.find({})]
# for student in students:
#     print(students)


from database import Database
from menu import Menu
from models.blog import Blog
# from models.post import Post

Database.initialize()

# blog = Blog(author='Himanshu', title='great title', description='blog description')
#
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.from_mongo(blog.id)
#
# print(blog.get_posts())

menu = Menu()
menu.run_menu()