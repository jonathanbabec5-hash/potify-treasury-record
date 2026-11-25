# November 25, 2026 · POTIFY Public Treasury Record

**Question.** Help any reader verify a published treasury statement against a specific on-chain receipt.

**Source and change.** New public evidence format based on the existing POTIFY trust and treasury reporting work. A reference passing validation has the required shape; independent verification is a separate action.

**Observed result.** The commands below ran in a clean test context using local files and fixtures.

```sh
python3 -m unittest discover -s tests
```

**Next acceptance check.** A pending report must stay visibly pending until a dated reference supports the claim.

**Owner and decision.** Chance owns the public release and approves campaign copy. This is a new reporting format. Custody, current balances, vesting and signer control have not been audited here.

This dated record describes the developer package. Verify remote commit and tree in the publication receipt before announcing a GitHub release.
