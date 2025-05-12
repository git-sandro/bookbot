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

def sort_on(dict):
    return dict["amount"]

def print_report(book_text, filepath):
    keys_n_values = count_amount_chars(book_text)
    sorted_list = []  
    print_entry = ""  

    title = "============ BOOKBOT ============\nAnalyzing book found at " + filepath + "...\n"
    word_count = "----------- Word Count ----------\nFound " + str(count_words(book_text)) + " total words\n"
    character_count = "--------- Character Count -------\n"

    for key_value in keys_n_values:
        sorted_list.append({"char": key_value, "amount": keys_n_values[key_value]})
    
    sorted_list.sort(reverse=True, key=sort_on)

    for entry in sorted_list:
        if entry["char"].isalpha() and entry["char"] != "\n":
            print_entry += str(entry["char"]) + ": " + str(entry["amount"]) + "\n"

    print_entry += "============= END ==============="
    return str(title + word_count + character_count + print_entry)
