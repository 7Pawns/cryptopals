import base64
from challenge3 import single_byte_key_xor_crack

def hamming_distance(text1: bytes, text2: bytes):
    return sum((a ^ b).bit_count() for a, b in zip(text1, text2))

def parse_b64_file(fname):
    with open(fname, 'r') as f:
        return base64.b64decode(f.read())

def get_possible_keysizes(data: bytes, keysize_count: int, keysize_range: range):
    possible_solutions = []
    is_sorted = False
    for keysize in keysize_range:
        if not is_sorted and len(possible_solutions) == keysize_count:
            possible_solutions.sort(key=lambda a: a[1])
            is_sorted = True
        
        i = 0
        normal_dists = []
        for i in range(0, len(data), keysize):
            if i+keysize*2 < len(data):
                normal_dists.append(
                    hamming_distance(data[i:i+keysize], data[i+keysize:i+keysize*2]) / keysize
                    )
            elif i+keysize < len(data) - 1:
                normal_dists.append(
                    hamming_distance(data[i:i+keysize], data[i+keysize:len(data)]) / keysize
                    )
            else:
                break
        avg_normal_dist = sum(normal_dists) / len(normal_dists)
        
        if not is_sorted:
            possible_solutions.append((keysize, avg_normal_dist))
        elif possible_solutions[keysize_count-1][1] > avg_normal_dist:
            possible_solutions[keysize_count-1] = (keysize, avg_normal_dist)
            possible_solutions.sort(key=lambda a: a[1]) # sucks for performance but idc for now
    return possible_solutions
    
def break_data_to_blocks(data: bytes, block_length: int):
    return tuple(data[i:i+block_length] for i in range(0, len(data), block_length))

def repeating_xor_key_decrypt(data: bytes, key: bytes):
    decrypted = b''
    keysize = len(key)
    for i, byte in enumerate(data):
        decrypted += (byte ^ key[i%keysize]).to_bytes(1)
    return decrypted

def repeating_xor_key_crack(data: bytes, keysize_count: int, keysize_range: range, attempt_optimize=False):
    possible_keysizes = get_possible_keysizes(data, keysize_count, keysize_range)
    print("Using possible keysizes and their hamming distances:", possible_keysizes)
    
    # start from smallest keysize to potentially do less work
    if attempt_optimize:
        keysizes = sorted(tuple(x[0] for x in possible_keysizes))
    else:
        keysizes = tuple(x[0] for x in possible_keysizes)
    
    keys = []
    for keysize in keysizes:
        key = b''
        blocked_data = break_data_to_blocks(data, keysize)
        for i in range(keysize):
            single_byte_transposed_blocks = bytes(blk[i] if i < len(blk) else 0x0 for blk in blocked_data)
            key += single_byte_key_xor_crack(single_byte_transposed_blocks)[2].to_bytes(1)

        keys.append(key)
    
    return keys
    
if __name__ == "__main__":
    text1 = "this is a test"
    text2 = "wokka wokka!!!"

    assert hamming_distance(text1.encode(), text2.encode()) == 37
    print("Hamming distance Correct")

    keys = repeating_xor_key_crack(parse_b64_file('./6.txt'), 3, range(2, 41))
    print("Possible keys", keys)
    # can go further and attempt to find the most english like text after key decryption 
    # but for now this is enough
    
    print(repeating_xor_key_decrypt(parse_b64_file('./6.txt'), keys[0]).decode())

    


