from math import log2

def get_huffman_codes(char_dict):
    chars_codes = dict(zip(list(map(lambda x: x[0], char_dict)), [''] * len(char_dict)))
    dictionary = [([x[0]], x[1]) for x in char_dict]
    while len(dictionary) > 1:
        dictionary.sort(key=lambda x: -x[1])
        for char in dictionary[-2][0]:
            chars_codes[char] += '0'
        for char in dictionary[-1][0]:
            chars_codes[char] += '1'
        #print(dictionary[-2][0])
        new_node = []
        new_node.extend(dictionary[-2][0])
        new_node.extend(dictionary[-1][0])
        new_item = (new_node, dictionary[-2][1] + dictionary[-1][1])
        dictionary.pop()
        dictionary.pop()
        dictionary.append(new_item)
    return chars_codes


def lzw_encode(txt, characters):
    dictionary = characters.copy()
    codes = []
    cur_string = ''
    for char in txt:
        cur_string += char
        if cur_string not in dictionary:
            dictionary.append(cur_string)
            codes.append(dictionary.index(cur_string[:-1]))
            cur_string = char
    codes.append(dictionary.index(cur_string))
    max_code = max(codes)
    lzw_code = ''
    for code in codes:
        lzw_code += bin(code)[2:].zfill(len(bin(max_code)[2:]))
    return lzw_code


f = open('text.txt', 'r')
text = f.read().lower()
print('Text len:', len(text))
chars = {}
for char in text:
    if char not in chars.keys():
        chars[char] = 1
    else:
        chars[char] += 1
chars = list(chars.items())
print('Unique characters:', len(chars))
chars.sort(key=lambda x: x[1])
for char, freq in chars:
    print(f"'{char}':", freq)
print('Remove the 3 rarest ones:', end=' ')
rarest = list(map(lambda x: x[0], chars[:3]))
print(rarest)
chars = list(filter(lambda x: x[0] not in rarest, chars))
for char in rarest:
    text = text.replace(char, '')
print('Now our text has length:', len(text), ' and consists from: ')
for char, freq in chars:
    print(f"'{char}':", freq)
pairs = {}
for i in range(0, len(text), 2):
    if text[i] + text[i + 1] not in pairs.keys():
        pairs[text[i] + text[i + 1]] = 1
    else:
        pairs[text[i] + text[i + 1]] += 1
pairs = list(pairs.items())
print('Unique pairs:', len(pairs))
pairs.sort(key=lambda x: x[1])
for pair, freq in pairs:
    print(f"'{pair}':", freq)

print('Encode our text with Huffman\'s algorithm:')
huffman_codes_chars = get_huffman_codes(chars)
huffman_code_chars = ''
for char in text:
    huffman_code_chars += huffman_codes_chars[char]
print('By char:')
print(huffman_code_chars)
huffman_codes_pairs = get_huffman_codes(pairs)
huffman_code_pairs = ''
for i in range(0, len(text), 2):
    huffman_code_pairs += huffman_codes_pairs[text[i] + text[i + 1]]
print('By pair')
print(huffman_code_pairs)
print('Huffman code by char length:', len(huffman_code_chars))
print('Huffman code by pair length:', len(huffman_code_pairs))
text_info = 0
for _, freq in chars:
    text_info -= freq / len(text) * log2(freq / len(text))
print('Amount of information in text: ', text_info)
huffman_info_char = 0
for char in chars:
    huffman_info_char += char[1] * len(huffman_codes_chars[char[0]])
huffman_info_char /= len(text)
print('Huffman by char:', huffman_info_char)
print('Now encode our text with LZW algorithm:')
lzw_code = lzw_encode(text, list(map(lambda x: x[0], chars)))
print(lzw_code)
print('LZW code length:', len(lzw_code))
print('Uniform code length:', 5 * len(text))
