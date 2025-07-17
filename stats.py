import sys

def get_book_text(path_to_file):

    #with open("/home/stephen/workspace/github.com/SteveGit16/bookbot/books/frankenstein.txt") as f:


    
    with open(sys.argv[1], "r") as f:
        file_contents = f.read()
        
        words = file_contents.split()

        num_words = -1

        for word in words:
            num_words += 1
            
        return num_words


def char_count(path_to_file):

    #with open("/home/stephen/workspace/github.com/SteveGit16/bookbot/books/frankenstein.txt") as f:
    with open(sys.argv[1], "r") as f:
        
        file_contents = f.read()             
        char_dict = {}                
                                                       
        for char in file_contents:
            lower_char = char.lower()

            if lower_char .isalpha():

                if lower_char not in char_dict:
                    char_dict[lower_char] = 1

                else:
                    char_dict[lower_char] += 1
                   
              
        return char_dict


def sort(char_dict):

    items = list(char_dict.items())

    for char, count in sorted(char_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{char}: {count}")

    
    return items

