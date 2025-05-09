from stats import count_words, count_amount_chars

def get_book_text(filepath):
    with open(filepath) as book_text:
        return book_text.read()

def main():
    #print(f"{count_words(get_book_text('books/frankenstein.txt'))} words found in the document")
    print(count_amount_chars(get_book_text('books/frankenstein.txt')))
main()