def sort(sorting):
    pass

def count_char(file):
    chars = {}
    for letter in file:
        lower = letter.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    
    return chars


    

def count_words(file):

        words = file.split()
        count = len(words)

            
        print(f"Found {count} total words")
        
    

def get_book_text(path):
        file_contents = ""
        with open(path) as f:
        
            file_contents = f.read()
        return file_contents
        