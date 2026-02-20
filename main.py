from stats import addDict, count_words, get_book_text, count_char, sort_on

def main():
    text = get_book_text("books/frankenstein.txt")
    
    result = addDict(count_char(text))
    output = sort_on(result)
    print(output)

    

main()
