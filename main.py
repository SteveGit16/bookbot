import sys
from stats import get_book_text, char_count, count_words, sort_characters 

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)                  
                        
    book_path = sys.argv[1]

    text = get_book_text(book_path)       
    word_count = count_words(text)
    character_counts = char_count(book_path)
    sorted_chars = sort_characters(character_counts)         #New variable name sorted_chars is using sort_characters function.

    #Print Report now:

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")


    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"{char}: {count}")

    print("============= END ===============")

main()
