def word_count(text):
    count = len(text.split())
    return count

def char_count(text):
    mapping = {}
    for ch in text.lower():
        if ch not in mapping:
            mapping[ch] = 1
        else:
            mapping[ch] = mapping[ch] + 1
    return mapping