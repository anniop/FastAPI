# In this project we are just dealing with the request methods.
from fastapi import FastAPI, HTTPException
from enum import Enum
from typing import Optional

app = FastAPI()

BOOKS = {
    "book_1": {"title": "Book One", "author": "Author One"},
    "book_2": {"title": "Book Two", "author": "Author Two"},
    "book_3": {"title": "Book Three", "author": "Author Three"},
    "book_4": {"title": "Book Four", "author": "Author Four"},
    "book_5": {"title": "Book Five", "author": "Author Five"},
    "book_6": {"title": "Book Six", "author": "Author Six"},
    
}

class Direction_Name(str, Enum):
    north  = "North"
    south = "South"
    east = "East"
    west = "West"

# This Function will not display the book that you dont want to see and it will show all the remaining books
@app.get("/")
async def read_all_books(skip_book: Optional[str] = None): # the use of optional is if the user want to leave the input empty then optional is used
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books   
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title):
    return {"book_title" : book_title}

@app.get("/books/{fav_books}")
async def read_fav_books(fav_books):
    return {"book_title": fav_books}

@app.get("/book/{book_id}")
async def read_id(book_id : int):
    return {"book_ID" : book_id}

  

@app.get("/{book_name}")
async def return_book(book_name: str):
    if book_name in BOOKS:
        return BOOKS[book_name]
    else:
        raise HTTPException(status_code=404, detail="Book not found")
    

@app.post("/")  # This API call of post method will create a new book 
async def create_book(book_title,book_author):
    current_book_id = 0

    if(len(BOOKS) > 0):
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x
    BOOKS[f"book_{current_book_id + 1}"] = {'title' : book_title, 'author' : book_author}
    return BOOKS[f'book_{current_book_id + 1}']

@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str): # this are the parameters we are passing to the function
    book_info = {'title': book_title, 'author': book_author} # This will take two parameters for us title,author
    if book_name in BOOKS:
        BOOKS[book_name] = book_info    # the saved information will be saved in the "BOOKS" dictonary 
        return book_info
    else:
        return {"error": "Book not found"}

@app.get("/assignment/")
async def read_books(book_name : str):
    return {"book_title" : book_name}

@app.delete("/{book_name}/")
async def delete_book(book_name: str):
    if book_name in BOOKS:
        del BOOKS[book_name]
        return {"message": f"Book '{book_name}' deleted"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/assignment")
async def delete(book_name):
    del BOOKS[book_name]
    return BOOKS


