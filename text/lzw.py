def lzw_encode(text):
    dictionary = {chr(i): i for i in range(256)}
    code = 256
    w = ""
    result = []

    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = code
            code += 1
            w = c
    if w:
        result.append(dictionary[w])
    return result

def lzw_decode(encoded):
    dictionary = {i: chr(i) for i in range(256)}
    code = 256
    w = chr(encoded[0])
    result = [w]

    for k in encoded[1:]:
        entry = dictionary.get(k, w + w[0])
        result.append(entry)
        dictionary[code] = w + entry[0]
        code += 1
        w = entry
    return "".join(result)