from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from challenge6 import parse_b64_file

def aes_ecb_decrypt(data: bytes, key: bytes):
    cipher = Cipher(algorithms.AES128(key), modes.ECB())
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize()

if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"
    print(aes_ecb_decrypt(parse_b64_file('./7.txt'), key).decode())
    
    
    
