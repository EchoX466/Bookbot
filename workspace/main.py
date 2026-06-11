from stats import word_count

def get_book_text():
  with open("books/frankenstein.txt") as f:
    print(f.read())

def main():
  get_book_text()

word_count()

if __name__ == "__main__":
  main()
