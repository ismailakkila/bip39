from secrets import randbelow
from bip39 import Mnemonic
from bip39_helper import N, sha256
from os import path, remove
import pytest

MNEMONIC_SECRET = randbelow(N)
MNEMONIC_FILENAME = "mnemonic_unit_test"

@pytest.fixture
def mnemonic():
    m = Mnemonic(MNEMONIC_SECRET)
    print(m)
    return m

def test_mnemonic_structure(mnemonic):
    assert mnemonic.secret < N
    assert len(mnemonic.checksum) == 1
    assert sha256(mnemonic.secret.to_bytes(32, "big"))[0] == mnemonic.checksum[0]
    assert len(mnemonic.num_groups) == 24
    assert len(mnemonic.word_groups) == 24

def test_write_to_file(mnemonic):
    mnemonic.write_to_file(MNEMONIC_FILENAME)
    assert path.isfile(MNEMONIC_FILENAME) == True

def test_parse_from_file(mnemonic):
    m = Mnemonic.parse_from_file(MNEMONIC_FILENAME)
    assert m.secret == mnemonic.secret
    assert m.checksum == mnemonic.checksum
    assert m.num_groups == mnemonic.num_groups
    assert m.word_groups == mnemonic.word_groups

def test_parse(mnemonic):
    m = Mnemonic.parse(mnemonic.word_groups)
    assert m.secret == mnemonic.secret
    assert m.checksum == mnemonic.checksum
    assert m.num_groups == mnemonic.num_groups
    assert m.word_groups == mnemonic.word_groups

def test_delete_file(mnemonic):
    remove(MNEMONIC_FILENAME)
    assert path.isfile(MNEMONIC_FILENAME) == False

