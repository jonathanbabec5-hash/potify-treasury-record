# POTIFY Public Treasury Record

## Find your way in

| If you are… | Start here | Try this |
| --- | --- | --- |
| A reader | [Inspect the synthetic record](examples/record.json) | See which fields remain pending. |
| A developer | [Read the validator](src/record.py) | Distinguish a valid report format from evidence of a real balance. |
| A reviewer | [Explore the project tree](docs/DIRECTORY.md) | Propose a fixture that keeps unsupported claims pending. |

[Complete repository directory tree](docs/DIRECTORY.md)

## What ‘pending’ ought to look like

A public record is sometimes most useful before it contains a number. The sample treasury statement leaves its slot and reference empty. That tells the reader exactly which evidence is missing and gives the next reviewer something concrete to check.

The [synthetic record](examples/record.json) and the [validator](src/record.py) distinguish the shape of a report from the truth of a financial claim. Valid JSON cannot establish ownership, custody, a current balance or vesting. This repository supplies a reporting specification.

Review the sample as written. Is ‘pending’ still unmistakable after rendering? Suggest a clearer label or a fixture that keeps an unsupported claim pending. Public contributions need no real balances, private addresses, signer details or treasury records.

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
