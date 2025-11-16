from stats import word_count, char_count, sortaable_data


def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def print_report(loc,word_count, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {loc}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for ch in chars:
        print(f"{ch["char"]}: {ch["num"]}")

def main():
    content_loc = "books/frankenstein.txt"
    contents = get_book_text(content_loc)
    num_words = word_count(contents)
    num_chars = char_count(contents)
    printable = sortaable_data(num_chars)
    print_report(content_loc,num_words,printable)


main()