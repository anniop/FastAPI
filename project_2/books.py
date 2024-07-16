from fastapi import FastAPI
from pydantic import BaseModel # this library helps in data validation and setting management pydantic is useful because it enforces typehints at runtime and provides the user friendly errors   when data validation
from uuid import UUID   # Universal unique identifier 128 bit label which will be used for making primary key in the list.
from pydantic import Field
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    id:UUID
    title:str = Field(min_length=1)
    author:str = Field(min_length=1,max_length=100)
    description:Optional[str] = Field(title="Description of the book", max_length=100,min_length=1)
    rating:int = Field(gt=-1, lt=10) # Greater than & Less Than

    class Config: # This class will add the information below as the default values
        schema_extra = {
            "example":{
                "id":"1712cf7e-0288-4522-9206-f14f0c3d7d0d",
                "title" : "Computer Science Pro",
                "author" : "Aniket",
                "description" : "Nice",
                "rating" : 7
            }
        }

BOOKS = []

@app.get("/")
async def read_all_books(books_to_return : Optional[int] = None):
    if len(BOOKS) < 1:
        creat_book_no_api()
    
    if books_to_return and len(BOOKS) >= books_to_return > 0: # This will return the number of books entered by the user
        i = 1
        new_books=[]
        while i <= books_to_return:
            new_books.append(BOOKS[i-1])
            i += 1
        return new_books
    return BOOKS

@app.get("/book/{book_id}") #  This api call will return a specific book that the user needs on the basis of the UUID of the book
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x


@app.post("/") # this api call will add a book to the Book dictionary and then it will return it to the user.
async def create_book(book:Book):
    BOOKS.append(book)
    return book 

@app.put("/{book_id}") # This api call is use to update a books details 
async def update_book(book_id:UUID, book:Book):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter -1 ] = book
            return BOOKS[counter -1]

@app.delete("/{book_id}")
async def delete_book(book_id:UUID):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter -1]
            return f'ID:{book_id} Deleted'

def creat_book_no_api():
    book_1 = Book(id="4712cf7e-0288-4522-9206-f14f0c3d7d0d",
                  title="Title 1",author="Author 1", description="descritpion 1"
                  ,rating=9)
    book_2 = Book(id="c46b0c2f-7823-4295-8a81-9923a1ca3fde",
                  title="Title 2",author="Author 2", description="descritpion 2"
                  ,rating=7)
    book_3 = Book(id="c49d5f16-2241-4822-957d-6f4adc373369",
                  title="Title 3",author="Author 3", description="descritpion 3"
                  ,rating=6)
    book_4 = Book(id="ad042eb3-ee07-4926-8ec5-cc9eedc403c3",
                  title="Title 4",author="Author 4", description="descritpion 4"
                  ,rating=5)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
    
    