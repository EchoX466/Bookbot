from stats import word_count, get_chars_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count()
    print(f"{num_words} words found in the document")
    chars_dict = get_chars_dict(text)
    print(chars_dict)

if __name__ == "__main__":
    main()
