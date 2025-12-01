POINTS: 340 
🏆SOLVES: 9 
📝 DESCRIPTION: ARCADE OVERDRIVE - BOSS GATE LEVEL 1 The year is 20XX. You stand before the first Boss Gate of the legendary Arcade Overdrive tournament. Four guardians protect the entrance, each more powerful than the last. Legends speak of hackers turned away by its defenses. Some say it reads intentions. Others claim it speaks in tongues no parser understands. A few whisper about weaknesses in ancient authentication rituals. The final boss holds the Master Override Code. Defeat all guardians to claim it and advance to the next level. 
Author: Angel911 
FILES: 📁 bossgate.rar
When you get in the webpage you find {"game":"ARCADE OVERDRIVE","version":"1.0","endpoints":["/register","/login","/config","/boss/level1","/boss/level2","/boss/level3","/boss/level4"]}
This is very important — it means the challenge exposes internal API endpoints.
I opened the app folder with vs code and navigated to auth.py and found this truncated_hmac = full_hmac[:2] 
Only the first 2 bytes (16 bits) of the HMAC are used.
That means:
.HMAC security reduced from 256 bits → 16 bits
.Only 65,536 possible HMAC values
.Token structure is predictable and brute‑forceable
.We can generate an admin token 
The goal is to escalate from guest → admin, bypass rate limits, bypass the WAF, and retrieve the final flag from:

GET /boss/ﬂag?token=<token>
Exploitation steps:
I wrote an automated brute-forcer to find the 2-byte suffix.
However The challenge applies rate limiting per IP.
But the application trusts the X-Forwarded-For header without sanitization.
Thus:
headers = { "X-Forwarded-For": f"10.0.0.{random.randint(1,255)}" }
So that 
.Every request appears to come from a different fake internal IP.
.Rate limiting never triggers.
The WAF blocks:
/boss/flag
But the real endpoint in the code is: @router.get("/boss/ﬂag")  # notice the weird 'ﬂ'
The route uses "ﬂ" = Unicode U+FB02 (LATIN SMALL LIGATURE FL).

The WAF normalizes using NFC, but "ﬂ" ≠ "fl".
Thus the valid route bypasses the filter entirely.
Successful path: /boss/ﬂag
Final Exploitation Script is under exploit.py