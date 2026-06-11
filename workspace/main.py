def get_book_text():
  with open("books/frankenstein.txt") as f:
    print(f.read())

def word_count():
  with open("books/frankenstein.txt") as e:
    book = e.read()
    num_words = len(book.split())
    print(f"Found {num_words} total words")

def main():
  get_book_text()

if __name__ == "__main__":
  main()
