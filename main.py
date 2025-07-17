import sys
from stats import get_book_text, char_count, sort 

def main():

    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = "./books/frankenstein.txt"        #Remove hard coded book path here?  This creates an issue with following code
    get_book_text(path)                      #------couldn't find path error ---- if I remove the 'path =' line
    char_count(path)                         #------couldn't find path error ---- if I remove the 'path =' line

    book_path = sys.argv[1]               #created variable to store the path as first argument in the sys.argv
    text = get_book_text(book_path)       #created variable to store path

    character_counts = char_count(path)
    sort(character_counts)

    num_words = get_book_text(path)             

    print(f"Found {num_words} total words")

    

main()
