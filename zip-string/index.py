def zip_string(string):
    if len(string) == 0 or string is None:
        raise Exception('provided string is invalid')
    result = ''
    cur_char = string[0]
    cur_char_length = 0

    for i in range(len(string)):
        char = string[i]
        if i == len(string) - 1 or char != cur_char:
            if i == len(string) - 1:
                cur_char_length += 1
            result = f"{result}{cur_char}" if cur_char_length <= 1 else f"{result}{cur_char}{cur_char_length}"
            cur_char = char
            cur_char_length = 0
        cur_char_length += 1
    return result

print(zip_string('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB') == 'A6F7ZYX')
print(zip_string('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB') == 'A4B3C2XYZD4E3F3A6B28')
