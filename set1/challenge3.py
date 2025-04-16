import binascii
import string

letter_frequency_order_lower = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd',
                          'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b',
                          'v', 'k', 'j', 'x', 'q', 'z']
letter_frequency_order_lower.reverse()

letter_frequency_order_upper = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D',
                                'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B',
                                'V', 'K', 'J', 'X', 'Q', 'Z']
letter_frequency_order_upper.reverse()

def single_byte_key_xor_crack(hex_bytes: bytes):
    correct = (b"", 0, '')
    for char in range(0xff):
        potential_solution = b""
        score = 0
        for byte in hex_bytes:
            cur = byte ^ char
            potential_solution += (cur).to_bytes(1)
            if chr(cur) in string.ascii_lowercase:
                score += letter_frequency_order_lower.index(chr(cur))
            elif chr(cur) in string.ascii_uppercase:
                score += letter_frequency_order_upper.index(chr(cur))
            elif chr(cur) in " '":
                score += 1

        if score > correct[1]:
            correct = (potential_solution, score, char)
    return correct

if __name__ == "__main__":
    hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print(single_byte_key_xor_crack(binascii.unhexlify(hex_str.rstrip())))

        

    

        
