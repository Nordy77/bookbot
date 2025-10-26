def get_num_words(words):
    total = 0
    for word in words.split():
        total += 1
    return total

def count_chars(chars):
    char_dict = {}
    list_chars = []
    total_chars = 0
    for char in chars.lower():
        list_chars.append(char)
    for char in list_chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1 
    return char_dict
