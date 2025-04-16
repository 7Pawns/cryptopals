import binascii
from challenge6 import break_data_to_blocks

def detect_aes_ecb_mode(fname: str):
    ecb_mode_lines = []
    with open(fname, 'r') as f:
        for line in f:
            data = binascii.unhexlify(line.rstrip())
            blocked_data = break_data_to_blocks(data, 16)
            if len(blocked_data) != len(set(blocked_data)):
                ecb_mode_lines.append(line)
    return ecb_mode_lines
            

if __name__ == "__main__":
    print(detect_aes_ecb_mode('./8.txt'))
