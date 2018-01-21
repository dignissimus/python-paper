MAX_BYTES = 2
MAX_BITS = MAX_BYTES * 8
LONGER_THAN = 2

list_file = open(f"standard/short/shuf/enneeded{LONGER_THAN}", "r")
words = list(filter(lambda word: word.strip() != "", list_file.read().split("\n")))
list_file.close()


def group(array, group_length):
    length = 0
    buffer = []
    current = []
    for byte in array:
        if length == group_length:
            buffer.append(current)
            current = []
            length = 0
        current.append(byte)
        length += 1

    if current:
        buffer.append(current)
    return buffer


def to_words(array, byteorder="big"):
    grouped = group(array, MAX_BYTES)
    numericals = []
    for array in grouped:
        numericals.append(int.from_bytes(array, byteorder=byteorder))
    word_list = map(lambda x: words[x], numericals)
    paper = " ".join(word_list)

    return paper


def from_words(paper, byteorder="big"):
    numericals = []
    for word in paper.split(" "):
        word = word.strip()
        value = words.index(word)
        numericals += value.to_bytes(MAX_BYTES, byteorder=byteorder)
    return numericals
