def crc_8(text, polinom):
    ret = 0
    for i in text.encode():
        ret ^= i
        for j in range(8):
            if bin(ret)[2:].zfill(8)[-8] == '1':
                ret = (ret << 1)^polinom
            else:
                ret = (ret << 1)
    return hex(int(bin(ret)[2:][-8:], 2))[2:]
text = '123456789'#input()
polinom = [0xD5, 0xAB, 0xEA]
hash_text = crc_8(text, polinom[0])
print(hash_text.upper())
