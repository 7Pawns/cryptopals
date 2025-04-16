import binascii

def repeating_key_xor(text: str, key: bytes):
    key_length = len(key)
    cur_key_byte = 0
    enc_text = b""
    for byte in text.encode():
        enc_text += (byte ^ key[cur_key_byte]).to_bytes(1)
        cur_key_byte = (cur_key_byte + 1) % key_length
    return enc_text

if __name__ == "__main__":
    text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b'ICE'
    answer = b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    print(binascii.b2a_hex(repeating_key_xor(text, key)) == answer)