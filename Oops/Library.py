class Book:
    
   def __init__(self,b_id,b_name,author):
      self.id=b_id
      self.name=b_name
      self.author=author

class Library:

   def __init__(self,books,address):
      self.books=books
      self.address=address
   
   def get_authors_count(self):
      author_counts = {}
      for book in self.books:
         author = book.author.upper()
         author_counts[author] = author_counts.get(author, 0) + 1
      return author_counts

def get_books_by_city(city,library):
   for lib in library:
      if lib.address['city'].casefold()==city.casefold():
         return sorted(lib.books,key=lambda book:book.book_id,reverse=True)
   return None

# getting how many library objects
no_of_libraries=int(input())
libraries=[] #list of lib objects
for _ in range(no_of_libraries):
   total_books=int(input())
   books=[]
   for _ in range(total_books):
      id=int(input())
      name=input()
      author=input()
      book=Book(id,name,author)
      books.append(book)
   address={
      'street': input(),
      'area': input(),
      'city': input(),
      'state': input(),
      'zip': input()
   }

   library=Library(books,address)
   libraries.append(library)

author_count=libraries[0].get_authors_count()
for author,count in author_count:
   print(f"{author} {count}")
city_name=input()
book_list=get_books_by_city(city_name,libraries)

if book_list is None:
    print("No Book Found")
else:
    book_names = [book.name for book in book_list]
    print(book_names)

