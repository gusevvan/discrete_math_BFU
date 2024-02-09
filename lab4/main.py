from math import log2

def get_huffman_codes(char_dict):
    chars_codes = dict(zip(list(map(lambda x: x[0], char_dict)), [''] * len(char_dict)))
    dictionary = char_dict.copy()
    while len(dictionary) > 1:
        dictionary.sort(key=lambda x: -x[1])
        for char in dictionary[-2][0]:
            chars_codes[char] += '0'
        for char in dictionary[-1][0]:
            chars_codes[char] += '1'
        new_item = (dictionary[-2][0] + dictionary[-1][0], dictionary[-2][1] + dictionary[-1][1])
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

print('Encode our text with Huffman\'s algorithm:')
huffman_codes = get_huffman_codes(chars)
huffman_code = ''
for char in text:
    huffman_code += huffman_codes[char]
print(huffman_code)
print('Huffman code length:', len(huffman_code))
print('Amount of information in uniform code: ', log2(len(text)))
huffman_info = 0
for code in huffman_codes:
    huffman_info -= len(code) / 32 * log2(len(code) / 32)
print('Amount of information in Huffman code: ', huffman_info)
print('Now encode our text with LZW algorithm:')
lzw_code = lzw_encode(text, list(map(lambda x: x[0], chars)))
print(lzw_code)
print('LZW code length:', len(lzw_code))
print('Uniform code length:', 5 * len(text))
