def main():
    from stats import sort_chars
    from stats import get_num_words
    from stats import count_chars
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num = get_num_words(text)
    total_char = count_chars(text)
    sort = sort_chars(total_char)
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {num} total words")
    print("----------- Character Count ------")
    print(total_char)
    print(sort)
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
