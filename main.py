def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = get_char_dict(text)
    char_sorted_dicts = sorted_char_dict(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for dict in char_sorted_dicts:
        print(f"The '{dict["char"]}' character was found {dict["num"]} times")
        
    print("\n--- End of Report ---")


def get_book_text(path):
    with open(path, "r") as file:
        return file.read()


def count_words(text):
    words = text.split()

    return len(words)


def get_char_dict(text):
    char_dict = {}

    for char in text:
        char = char.lower()

        if not char.isalpha():
            continue

        if char not in char_dict:
            char_dict[char] = 1
            continue

        char_dict[char] += 1
    
    return char_dict


def sorted_char_dict(dict):
    sorted_list = []

    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    
    sorted_list.sort(reverse=True, key=lambda dictionary: dictionary["num"] )

    return sorted_list


main()

