def word_count():
  with open("books/frankenstein.txt") as e:
    book = e.read()
    num_words = len(book.split())
    print(f"Found {num_words} total words")


def get_chars_dict(text):
  lowered_strings = text.lower()
  chars_dict = {}
  for c in lowered_strings:
    if c in chars_dict:
      chars_dict[c] += 1
    else:
      chars_dict[c] = 1
  return chars_dict
