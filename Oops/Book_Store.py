class Book:
    
    def _init_(self,pages,price,author,Id,title):
        self.pages=pages
        self.price=price
        self.author=author
        self.Id=Id
        self.title=title
    
class BookStore:
    
    def _init_(self,BookList):
        self.BookList=BookList
    
    def findMinBookByid(self):
        """
        Input: BookList
        -------------
        Output:
        Return Book with minimum Id value
        
        """
        book_Ids=[book.Id for book in self.BookList]
        min_Id=min(book_Ids)
        for book in self.BookList:
            if min_Id is book.Id:
                return book
            else:
                return None
            
    
    def sortBookByid(self):
        
        """
        Input: BookList
        -------------
        Output:
        Return sorted book list with key=Id
        
        """
        book_Ids=[book.Id for book in self.BookList]
        if(len(book_Ids)!=0):
            return sorted(book_Ids)
        return None

no_of_books=int(input())
bookList=[]
for _ in range(no_of_books):
    pages=int(input())
    price=int(input())
    author=input()
    Id=int(input())
    title=input()
    book=Book(pages,price,author,Id,title)
    bookList.append(book)

bookstore=BookStore(bookList)

book=bookstore.findMinBookByid()
Ids=bookstore.sortBookByid()
if((book is None) or (Ids is None)):
    print("No Data Found")

else:
    for item in book:
        print(item)

    for Id in Ids:
        print(Id)