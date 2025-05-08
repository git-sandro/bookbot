from stats import count_words

def get_book_text(filepath):
    with open(filepath) as book_text:
        return book_text.read()

def main():
    words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{words} words found in the document")

main()