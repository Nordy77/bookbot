def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"Found {num_words(text)} total words")

def num_words(words):
    total = 0
    for word in words.split():
        total += 1
    return total
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
