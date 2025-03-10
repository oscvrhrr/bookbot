def count_words(text):
    words = text.split()
    count = len(words)
    return count


def count_chars(text):
    char_count = {}
    for char in text:
        lchar = char.lower()
        if lchar in char_count:
            current_count = char_count[lchar]
            char_count[lchar] = current_count + 1
        else:
            char_count[lchar] = 1
    return char_count

def sorted_list(dic):
    chars_list = []
    for char, count in dic.items():
        if char.isalpha():
            chars_list.append({"char": char, "count":count})
        chars_list.sort(reverse=True, key=lambda item: item["count"])
    return chars_list

