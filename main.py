from stats import get_num_words
import sys

def count_characters(file_contents):
    chars = {}
    for char in file_contents:
        lowerCaseChar = char.lower()
        if lowerCaseChar.isalpha() == False:
            continue
        if lowerCaseChar in chars:
            chars[lowerCaseChar] += 1
        else:
            chars[lowerCaseChar] = 1
    return chars

def get_character_count(file_contents):
    chars = {k: v for k, v in reversed(sorted(count_characters(file_contents).items(), key=lambda item: item[1]))}
    for char in chars:
        print(f"{char}: {chars[char]}")
            

def main():
    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    path_to_file = f"./{book}"
    with open(path_to_file) as f:
        print("============ BOOKBOT ============")
        file_contents = f.read()
        print(f"Analyzing book found at {book}")
        print("----------- Word Count ----------")
        get_num_words(file_contents)
        print("--------- Character Count -------")
        get_character_count(file_contents)    

main()