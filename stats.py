def get_num_words(book):
    return len(book.split())


def sort_on(dict):
    return dict["num"]


def count_chars(book):
    char_dict = {}

    for char in book:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict


def arrange_char_count(char_dict):
    char_list = []

    for char in char_dict:
        count = char_dict[char]
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_on)

    return char_list
