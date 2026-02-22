def addDict(dict1):
    Liste_dicts = []
    for k, v in dict1.items():
        if k.isalpha():
            element = {"char": k, "num": v}
            Liste_dicts.append(element)
        else:
            continue
    Liste_dicts.sort(reverse=True, key=sort_on)
    return Liste_dicts



def sort_on(mydict):
    return mydict["num"]

   

    

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

            
        return count
        
    

def get_book_text(path):
        file_contents = ""
        with open(path) as f:
        
            file_contents = f.read()
        return file_contents
        