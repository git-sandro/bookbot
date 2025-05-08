def get_book_text(filepath):
    with open(filepath) as book_text:
        return book_text.read()
    
def main():
    print(get_book_text("books/frankenstein.txt"))

main()