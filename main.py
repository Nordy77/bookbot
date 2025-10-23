def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"Found {num_words(text)} total words")

def num_words(words):
    for word in words:
        return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
