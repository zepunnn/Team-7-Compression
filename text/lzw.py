from utils_progress import progress


def lzw_encode(text):
    # Initialize dictionary with single characters
    dictionary = {chr(i): i for i in range(256)}
    dict_size = 256

    w = ""
    result = []

    for c in progress(text, "LZW Encoding", "char"):
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            # w is guaranteed to be in dictionary
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    if w:
        result.append(dictionary[w])

    return result


def lzw_decode(codes):
    dictionary = {i: chr(i) for i in range(256)}
    dict_size = 256

    w = dictionary[codes[0]]
    result = w

    for k in progress(codes[1:], "LZW Decoding", "code"):
        if k in dictionary:
            entry = dictionary[k]
        else:
            # Special LZW case
            entry = w + w[0]

        result += entry
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry

    return result