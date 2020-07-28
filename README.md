# BIP39 Implementation using Python

This is the BIP39 specification implementation for [Bitcoin](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki). It allows you to create a mnemonic sequence of 24 words from a secret and/or parse a 24 word list or file back to the same secret.

### Installation

```
pip install -r requirements
```

## Usage

**Create a mnemonic 24-word instance with a secret**
```
from secrets import randbelow
MNEMONIC_SECRET = randbelow(N)
m_random = Mnemonic(MNEMONIC_SECRET)
print(m_random)

Mnemonic (24 words):
[-] Secret: 8241902089993060732802436393950217117343760151742415816818594447477462641008
[-] Checksum: f4
[-] Words: banana ship below load clutch music gallery copper multiply allow dragon game wine sad diamond purse wine check rocket main danger churn place burden
```

**Write to file**
```
MNEMONIC_FILENAME = "mnemonic_unit_test"
m_random.write_to_file(MNEMONIC_FILENAME)
```

**Parse from file**
```
m_random = Mnemonic.parse_from_file(MNEMONIC_FILENAME)
```

**Parse from 24 word list**
```
m_random = Mnemonic.parse(m_random.word_groups)
```

## Tests
```
pytest --verbose bip39_test.py
```

## Acknowledgments and Resources

* [Programming Bitcoin](https://programmingbitcoin.com) by [Jimmy Song](https://github.com/jimmysong/programmingbitcoin)
