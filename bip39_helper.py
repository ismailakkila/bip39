"""This module contains BIP39 helper functions"""

import hashlib

N = (2**256) - (2**32) - 977

def sha256(payload):
    """This function returns the sha256 of the provided payload"""
    return hashlib.sha256(payload).digest()


def num_groups_1(payload):
    """This function returns the a list of 24 numbers representing the payload"""
    num_bits = len(payload) * 8
    num_groups = []
    payload_num = int.from_bytes(payload, 'big')
    iterations = num_bits // 11
    for _ in range(iterations):
        num = payload_num >> num_bits - 11 & 2047
        num_groups.append(num)
        payload_num <<= 11

    return num_groups


def num_groups_2(payload):
    """This function returns the a list of 24 numbers representing the payload"""
    num_groups = []
    read_count = 0
    num = 0
    for byte in payload:
        bit = 0
        while bit < 8:
            bit_enabled = byte & 128 == 128
            read_count += 1
            bit += 1
            if bit_enabled:
                num += 2 ** (11 - read_count)
            byte = byte << 1 & 255
            if read_count == 11:
                num_groups.append(num)
                read_count = 0
                num = 0

    return num_groups


def to_word_groups(num_groups):
    """
    This function returns the a list of 24 words from a list of 24 numbers
    representing the payload
    """
    with open('wordlist.txt', 'rb') as (file):
        words = file.readlines()
    words = [word.strip().decode('utf8') for word in words]
    word_groups = [words[num] for num in num_groups]
    return word_groups


def to_num_groups(word_groups):
    """
    This function returns the a list of 24 numbers from a list of 24 words
    representing the payload
    """
    with open('wordlist.txt', 'rb') as (file):
        words = file.readlines()
    words = [word.decode('utf8').strip() for word in words]
    num_groups = [words.index(word) for word in word_groups]
    return num_groups


def to_num_groups_from_file(filename):
    """
    This function returns the a list of 24 numbers from a file containing 24
    words (one per line) representing the payload
    """
    with open('wordlist.txt', 'rb') as (file):
        words = file.readlines()
    words = [word.decode('utf8').strip() for word in words]
    with open(filename, 'rb') as (file):
        word_groups = file.readlines()
    word_groups = [word.decode('utf8').strip() for word in word_groups]
    num_groups = [words.index(word) for word in word_groups]
    return num_groups
