"""This module allows you to create a 24 word BIP32 mnemonic from a secret"""

from bip39_helper import (
    N,
    sha256,
    num_groups_1,
    to_word_groups,
    to_num_groups,
    to_num_groups_from_file
)

class Mnemonic:
    """
    This class allows you to create a 24 word mnemonic instance 24
    from a secret
    """

    def __init__(self, secret):
        assert secret < N
        self.secret = secret
        secret_bytes = secret.to_bytes(32, "big")
        checksum_length = ((32 * 8) // 32) // 8
        self.checksum = sha256(secret_bytes)[:checksum_length]
        self.num_groups = num_groups_1(secret_bytes + self.checksum)
        self.word_groups = to_word_groups(self.num_groups)

    def __repr__(self):
        output = "Mnemonic (24 words):\n"
        output += "[-] Secret: {}\n".format(self.secret)
        output += "[-] Checksum: {}\n".format(self.checksum.hex())
        output += "[-] Words: {}\n".format(" ".join(self.word_groups))
        return output

    @classmethod
    def parse(cls, word_groups):
        """This function uses a 24 word list to instantiate a Mnemonic instance"""

        assert len(word_groups) == 24
        num_groups = to_num_groups(word_groups)
        total = 0
        for i, num in enumerate(num_groups):
            num_to_add = (num & 0b11111111111) << (11 * (23 - i))
            total += num_to_add
        total_bytes = total.to_bytes(33, "big")
        checksum = total_bytes[-1]
        assert sha256(total_bytes[:-1])[0] == checksum
        return cls(int.from_bytes(total_bytes[:-1], "big"))

    @classmethod
    def parse_from_file(cls, filename):
        """
        This function imports a file containing a 24 word list to instantiate
        a Mnemonic instance. The file should contain a word on each line for a
        total of 24 lines
        """

        num_groups = to_num_groups_from_file(filename)
        assert len(num_groups) == 24
        total = 0
        for i, num in enumerate(num_groups):
            num_to_add = (num & 0b11111111111) << (11 * (23 - i))
            total += num_to_add
        total_bytes = total.to_bytes(33, "big")
        checksum = total_bytes[-1]
        assert sha256(total_bytes[:-1])[0] == checksum
        return cls(int.from_bytes(total_bytes[:-1], "big"))

    def write_to_file(self, filename):
        """
        This function writes the 24 word list to a filename specifed in the same
        working directory
        """

        with open(filename, "wb") as handle:
            handle.write("\n".join(self.word_groups).encode("utf8"))
