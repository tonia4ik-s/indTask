from flask import Flask, jsonify, request
from entities.Library import Library, Book

app = Flask(__name__)
file_name = "library.txt"
library = Library({Book("Book1", "Author1"), Book("Book2", "Author2")}).book_set
book_id = 0


@app.route("/library", methods=["GET"])
def get_books():
    response_body = read_data_from_file()
    return jsonify(response_body)


@app.route("/get-books", methods=["POST"])
def create_books():
    request_body = request.json
    received_books = []

    for req in request_body:
        book = Book(req["title"], req["author"])
        received_books.append(book)
        library.add_book(book)

    write_all_entities_in_file(received_books, "a")
    received_books_set = list_to_json(received_books)
    return jsonify(received_books_set)


@app.route("/edit-book", methods="PUT")
def edit_book():
    request_body = request.json
    received_book_id = request_body[0]





def list_to_json(received_books):
    entities_set = []
    for book in received_books:
        entities_set.append(book.to_json())
    return entities_set


def read_data_from_file():
    entities_set = []
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            props = line.split(',')
            entities_set.append(to_json(props))
    return entities_set



def to_json(properties):
    return {"id": properties[0], "brand": properties[1], "memory": properties[2]}


def write_all_entities_in_file(data, mode):
    with open(file_name, mode) as f:
        for book in data:
            global book_id
            book_id = book_id + 1
            f.write(f"{book_id},{book.title},{book.author}")


if __name__ == "__main__":
    write_all_entities_in_file(library, "w")
    app.run("0.0.0.0", port=3333)
