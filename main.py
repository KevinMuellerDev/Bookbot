from stats import get_num_words, count_chars, arrange_char_count
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def output(path, word_count, arranged_data):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in range(0, len(arranged_data)):
        key = None
        count = None
        for data in arranged_data[i]:
            if data == "char":
                key = arranged_data[i][data]
            elif data == "num":
                count = arranged_data[i][data]
        print(f"{key}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    book = get_book_text(filepath)
    word_count = get_num_words(book)
    char_count = count_chars(book)
    arranged_data = arrange_char_count(char_count)
    output(filepath, word_count, arranged_data)


main()
