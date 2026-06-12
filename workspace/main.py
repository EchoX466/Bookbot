from stats import word_count, get_chars_dict, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
  # Establish word count and print to screen
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"Found {num_words} total words")

  # Call the function from stats.py to build a dictionary of characters and counts
    chars_dict = get_chars_dict(text)
    

  # Convert the dictionary to a list and sort
    sorted_chars = chars_dict_to_sorted_list(chars_dict)
    print(sorted_chars)
if __name__ == "__main__":
    main()
