import binascii

def fixed_xor(hex_str1, hex_str2):
    return binascii.hexlify(bytes(a ^ b for a, b in zip(binascii.unhexlify(hex_str1), binascii.unhexlify(hex_str2))))

if __name__ == "__main__":
    hex_str1 = "1c0111001f010100061a024b53535009181c"
    hex_str2 = "686974207468652062756c6c277320657965"
    print(fixed_xor(hex_str1, hex_str2))