import sys
from stats import addDict, count_words, get_book_text, count_char, sort_on


def main():
    if len(sys.argv) == 2:
        pass
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    count = count_words(text)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for d in addDict(count_char(text)):
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")

    

main()
