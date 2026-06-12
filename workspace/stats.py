def word_count(text):
    return len(text.split())


def get_chars_dict(text):
  lowered_strings = text.lower()
  chars_dict = {}
  for c in lowered_strings:
    if c in chars_dict:
      chars_dict[c] += 1
    else:
      chars_dict[c] = 1
  return chars_dict

def sort_on(book: tuple[str, int]) -> int:
  return book[1]


def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    char_list = []

    for char in char_dict:
        count = char_dict[char]
        char_list.append((char, count))

    sorted_list = sorted(char_list, key=sort_on, reverse=True)

    return sorted_list

