from stats import word_count, get_chars_dict, chars_dict_to_sorted_list
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
  # Establish book path, word count and print to screen
    if len(sys.argv) < 2:
      print(f"Usage: python3 main.py <path_to_book>")
      sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)

  # Call the function from stats.py to build a dictionary of characters and counts
    chars_dict = get_chars_dict(text)

  # Convert the dictionary to a list and sort
    sorted_chars = chars_dict_to_sorted_list(chars_dict)

    print_report(book_path, num_words, sorted_chars)

def print_report(book_path, num_words, sorted_chars):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    for char, count in sorted_chars:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")




if __name__ == "__main__":
    main()
