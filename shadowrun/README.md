Category: Crypto
Points: 100
Solves: 22
Author: Z3U55

📝 Challenge Description

FastJack hacked into the heavily protected Renraku Arcology to steal secret research files inside the Matrix.
But when he finally accessed the core, he discovered the files were encrypted.

FastJack failed…
Can you recover the flag?

The challenge provides two files output.txt and shadowrun.py:

n — a 1024‑bit RSA modulus

c — the ciphertext

The RSA encryption uses:

𝑐=𝑚^𝑒 mod n
 
However, the implementation contains a critical weakness:
it uses a small public exponent
⚠️ Why This Breaks RSA

The plaintext is a short flag (a few dozen bytes).
Thus the numeric value m is small.

If:

𝑚^3<𝑛 (as is the case here)

then RSA performs no modular reduction, and the encryption becomes:

𝑐=𝑚^3
This means the ciphertext is literally the cube of the plaintext.

🔓 Exploitation: Recovering the Plaintext
Since:
𝑐=𝑚^3
we simply compute the integer cube root of the ciphertext:
Then convert the resulting integer back into bytes to reveal the flag.
This completely bypasses the need for:
.factoring n
.computing φ(n)
.recovering the private key

It is an example of the low‑exponent RSA attack.

The full solving code used to recover the plaintext is available under:
solve.py
After running the script, we recover the flag:

CM{F45tJ4ck_tr1ck3d_U5_4ll}