from stats import count_words, get_book_text, count_char

def main():
    text = get_book_text("books/frankenstein.txt")
    
    result = count_char(text)
    print(result)

main()
