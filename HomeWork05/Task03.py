# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_mtd(string: str) -> str:
    """
    Basic logic for encoding
    :param string: str
    :return: string_out: str
    """
    string_out = ''
    count = 1
    while string:
        if len(string) > 1:
            if string[0] == string[1]:
                count += 1
                string = string[1:]
            else:
                string_out += str(count) + string[0]
                string = string[1:]
                count = 1
        else:
            string_out += str(count) + string[0]
            string = ''

    return string_out


def rle_bck(string: str) -> str:
    """
    Basic logic for decoding
    :param string: str
    :return: string_out: str
    """
    string_out = ''
    count = ''
    while string:
        if len(string):
            if string[0].isdigit():
                count += string[0]
                string = string[1:]
            else:
                count = int(count)
                string_out += string[0]*int(count)
                string = string[1:]
                count = ''
        else:
            break
    return string_out


def rle_dec(string: str) -> str:
    count = ''
    out_str = ''
    for i, c in enumerate(string):
        if c.isdigit():
            count += c
        else:
            out_str += string[i] * int(count)
            count = ''
    return out_str


# some changes
print(rle_mtd('ABCABCABCDDDFFFFFF'))    # from wikipedia 1A1B1C1A1B1C1A1B1C3D6F
print(rle_mtd('WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWW'))   # 9W3B24W1B15W
print(rle_bck(rle_mtd('WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWW')))
print(rle_dec(rle_mtd('WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWW')))
print(rle_bck(rle_mtd('ABCABCABCDDDFFFFFF')))
print(rle_dec(rle_mtd('ABCABCABCDDDFFFFFF')))
