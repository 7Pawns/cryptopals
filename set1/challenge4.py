import binascii
from challenge3 import single_byte_key_xor_crack

def find_encrypted_string(filename):
    correct = (b"", 0)
    with open(filename, 'r') as f:
        for line in f:
            possible_decrypted = single_byte_key_xor_crack(binascii.unhexlify(line.rstrip()))
            if possible_decrypted[1] > correct[1]:
                correct = possible_decrypted
        return correct

if __name__ == "__main__":  
    print(find_encrypted_string('4.txt'))