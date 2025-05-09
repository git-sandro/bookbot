def count_words(book_text):
    return len(book_text.split())

def count_amount_chars(book_text):
    chars_amount = {}
    for i in range(len(book_text)):
        char = book_text[i].lower()
        if char in chars_amount:
            chars_amount[char] += 1
        else:
            chars_amount[char] = 1
    return chars_amount