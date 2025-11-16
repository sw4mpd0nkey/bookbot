from stats import word_count, char_count

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    num_words = word_count(contents)
    print(f"Found {num_words} total words")
    num_chars = char_count(contents)
    print(f"{num_chars}")
main()