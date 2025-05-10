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
    chars_dictonary = count_amount_chars(book_text)
    list_dictonary = []
    sorted_list = []  
    print_entry = ""  

    title = "============ BOOKBOT ============\nAnalyzing book found at " + filepath + "...\n"
    word_count = "----------- Word Count ----------\nFound " + str(count_words(book_text)) + " total words\n"
    character_count = "--------- Character Count -------\n"

    for dictonary in chars_dictonary:
        list_dictonary.append([dictonary, chars_dictonary[dictonary]])

    for key_value in list_dictonary:
        sorted_list.append({"char": key_value[0], "amount": key_value[1]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    #del sorted_list[0]

    for entry in sorted_list:
        if entry["char"].isalpha() and entry["char"] != "\n":
            print_entry += str(entry["char"]) + ": " + str(entry["amount"]) + "\n"

    print_entry += "============= END ==============="
    return str(title + word_count + character_count + print_entry)

"""
boot.dev solution LMAO
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list"""