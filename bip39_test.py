from os import path, remove
from secrets import randbelow
import pytest
from bip39 import Mnemonic
from bip39_helper import N, sha256

MNEMONIC_SECRET = randbelow(N)
MNEMONIC_FILENAME = "mnemonic_unit_test"

@pytest.fixture
def mnemonic():
    m_random = Mnemonic(MNEMONIC_SECRET)
    print(m_random)
    return m_random

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
    m_random = Mnemonic.parse_from_file(MNEMONIC_FILENAME)
    assert m_random.secret == mnemonic.secret
    assert m_random.checksum == mnemonic.checksum
    assert m_random.num_groups == mnemonic.num_groups
    assert m_random.word_groups == mnemonic.word_groups

def test_parse(mnemonic):
    m_random = Mnemonic.parse(mnemonic.word_groups)
    assert m_random.secret == mnemonic.secret
    assert m_random.checksum == mnemonic.checksum
    assert m_random.num_groups == mnemonic.num_groups
    assert m_random.word_groups == mnemonic.word_groups

def test_delete_file():
    remove(MNEMONIC_FILENAME)
    assert not path.isfile(MNEMONIC_FILENAME)
