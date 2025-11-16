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

def sort_on(items):
    return items["num"]

def sortaable_data(my_data):
    data = []

    for d in my_data:
        data.append(
            {
                "char": d,
                "num": my_data[d] 
            })

    data.sort(reverse=True,key=sort_on)
    return data