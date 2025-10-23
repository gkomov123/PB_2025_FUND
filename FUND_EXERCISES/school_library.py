shelf_of_books = input().split("&")

while True:
    command_split = input().split(" | ")
    command = command_split[0]

    if command == "Done":
        break

    elif command == "Add Book":
        book_name = command_split[1]
        if book_name not in shelf_of_books:
            shelf_of_books.insert(0, book_name)

    elif command == "Take Book":
        book_name = command_split[1]
        if book_name in shelf_of_books:
            shelf_of_books.remove(book_name)

    elif command == "Swap Books":
        book_one, book_two = command_split[1], command_split[2]
        if book_one in shelf_of_books and book_two in shelf_of_books:
            book_one_index = shelf_of_books.index(book_one)
            book_two_index = shelf_of_books.index(book_two)
            shelf_of_books[book_one_index], shelf_of_books[book_two_index] = shelf_of_books[book_two_index], \
                shelf_of_books[book_one_index]

    elif command == "Insert Book":
        book_name = command_split[1]
        if book_name not in shelf_of_books:
            shelf_of_books.append(book_name)

    elif command == "Check Book":
        index = int(command_split[1])
        if index <= len(shelf_of_books):
            print(shelf_of_books[index])

print(", ".join(shelf_of_books))
