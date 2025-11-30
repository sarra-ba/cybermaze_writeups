Challenge overview:

We are given a folder that contains a hidden .git/ directory.
The challenge description implies that a secret (the flag) was stored somewhere in the Git history or Git internal objects.

So the goal is to inspect raw Git objects, decompress them, and search for a CM{...} flag.
Understanding Git Objects:

Inside .git/objects/ each file is a compressed Git object:

.git/objects/aa/bbcccccccc...
Each object is stored as:
zlib-compressed data
containing either:
.a commit
.a blob (file content)
.a tree
.a tag
.Git normally stores every version of every file ever committed—even if deleted later.

So flags often hide inside:
deleted file versions
old commits
unreferenced blobs
corrupted objects
And are still recoverable by scanning all objects.
Solution Strategy
✔️ Step 1 — Iterate through all Git object files
✔️ Step 2 — Decompress using zlib
✔️ Step 3 — Decode as text
✔️ Step 4 — Search for flag format: CM{…}

This can be automated through vault.py w i run it and i got 
==== OBJECT ====
 blob 3{}


==== OBJECT ====
 blob 331{
  "master_password_hash": "$2y$12$z8Y6X5V4U3T2S1R0Q9P8O7N6M5L4K3J2I1H0G9F8E7D6C5B4A3Z2Y1X",
  "passwords": {
    "gmail": "Disco1990Newyork",
    "bank": "GoldenCoins4444",
    "company-vpn": "MyVerySecureP@ss777",
    "super-secret-api": "CM{th3y_h4d_a_gr34t_t4st3_90s}"

    "You-need-me-later": "Pr0ducti0n_B4ckUP_K3Y!"
  }
}

🏁 Final Flag
CM{th3y_h4d_a_gr34t_t4st3_90s}