import hashlib

def sha256(s):
    return hashlib.sha256(s).digest()

def num_groups_1(payload):
    num_bits = len(payload) * 8
    num_groups = []
    payload_num = int.from_bytes(payload, "big")
    iterations = num_bits // 11
    for i in range(iterations):
        num = (payload_num >> num_bits - 11) & 0b11111111111
        num_groups.append(num)
        payload_num <<= 11
    return num_groups

def num_groups_2(payload):
    num_groups = []
    read_count = 0
    num = 0
    for byte in secret_bytes_checksum:
        bit = 0
        while bit < 8:
            bit_enabled = (byte & 128) == 128
            read_count += 1
            bit += 1
            if bit_enabled:
                num += 2**(11 - read_count)
            byte = byte << 1 & 255
            if read_count == 11:
                num_groups.append(num)
                read_count = 0
                num = 0
    return num_groups

def to_word_groups(num_groups):
    with open("wordlist.txt", "rb") as file:
        words = file.readlines()
    words = [word.strip().decode("utf8") for word in words]
    word_groups = [words[num] for num in num_groups]
    return word_groups

def to_num_groups(word_groups):
    with open("wordlist.txt", "rb") as file:
        words = file.readlines()
    words = [word.decode("utf8").strip() for word in words]
    num_groups = [words.index(word) for word in word_groups]
    return num_groups

def to_num_groups_from_file(filename):
    with open("wordlist.txt", "rb") as file:
        words = file.readlines()
    words = [word.decode("utf8").strip() for word in words]
    with open(filename, "rb") as file:
        word_groups = file.readlines()
    word_groups = [word.decode("utf8").strip() for word in word_groups]
    num_groups = [words.index(word) for word in word_groups]
    return num_groups
