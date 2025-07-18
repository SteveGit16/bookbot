import sys

def get_book_text(path_to_file):

    with open(path_to_file, "r") as f:
    
        file_contents = f.read()  
        words = file_contents.split()
        num_words = -1
        for word in words:
            num_words += 1
            
        
    return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def char_count(path_to_file):   
    with open(path_to_file, "r")as f:   
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

def sort_characters(char_dict):
    
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

        char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

