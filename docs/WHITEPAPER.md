# POTIFY Public Treasury Record
## Whitepaper · public developer edition

**November 25, 2026 · New public reporting specification**

### Goal and audience

Help any reader verify a published treasury statement against a specific on-chain receipt. The immediate audience is community members and independent reviewers.

### Design and implementation

A structured evidence format records asset, claim, observed slot, transaction reference and verification state. It keeps wallet-holder datasets and signer operations outside the report. Record when a claim was made and the slot used to substantiate it. A successful transaction can establish a transfer without establishing ongoing custody or entitlement.

### What a contributor can establish

The commands below ran in a clean test context using local files and fixtures. Require someone to reconcile asset, amount and destination before promoting a pending statement. A structural validator cannot inspect chain state.

### Evidence and outstanding work

This is a new reporting format. Custody, current balances, vesting and signer control have not been audited here. The next acceptance case is concrete. A pending report must stay visibly pending until a dated reference supports the claim.

### Place in POTIFY

Support trust in the ecosystem; trace any later shop referral separately. No direct treasury sales target. The marketing plan gives the test window and the evidence for a commercial outcome.

[Source provenance](source.json) · [Build log](BUILD-LOG.md) · [Marketing plan](MARKETING.md)
