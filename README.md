# POTIFY Public Treasury Record

[Complete repository directory tree](docs/DIRECTORY.md)

**New public reporting specification.** Help any reader verify a published treasury statement against a specific on-chain receipt.

### Setup and usage

Python 3.10 or newer. The project uses the standard library.

```sh
python3 src/record.py examples/record.json
```

Review one treasury claim against its source. 

### Developer entry points

A structured evidence format records asset, claim, observed slot, transaction reference and verification state. It keeps wallet-holder datasets and signer operations outside the report. Explore `examples/`, `src/`, `tests/` in the full tree.

### Verification

The commands below ran in a clean test context using local files and fixtures.

```sh
python3 -m unittest discover -s tests
```

### Release scope

This is a new reporting format. Custody, current balances, vesting and signer control have not been audited here. New public evidence format based on the existing POTIFY trust and treasury reporting work. A reference passing validation has the required shape; independent verification is a separate action.

[Technical whitepaper](docs/WHITEPAPER.md) · [Marketing and sales plan](docs/MARKETING.md) · [Dated developer log](docs/BUILD-LOG.md)

Existing asset and code terms remain applicable. Public access to a recording, illustration, brand or manuscript does not itself grant commercial reuse rights.
