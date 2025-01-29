

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

def main():
    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        
        print(f"--- Begin report of books/frankenstein.txt ---")
        total_words = len(file_contents.split())
        print(f"{total_words} words found in the document")
        chars = {k: v for k, v in reversed(sorted(count_characters(file_contents).items(), key=lambda item: item[1]))}
        for char in chars:
            print(f"The '{char}' character was found {chars[char]} times")
            

main()