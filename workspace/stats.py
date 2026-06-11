def word_count():
  with open("books/frankenstein.txt") as e:
    book = e.read()
    num_words = len(book.split())
    print(f"Found {num_words} total words")


