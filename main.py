def main():
    from stats import get_num_words
    from stats import count_chars
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num = get_num_words(text)
    char = count_chars(text)
    print(f"Found {num} total words")
    print(char)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
