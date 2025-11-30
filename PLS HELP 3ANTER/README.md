
Category: Web Exploitation
Author: BOU3RADA

Challenge overview:
The challenge provides a Flask-based game API. Users can log in, submit scores, and after 20 legitimate score submissions, the server returns a flag stored in the database.

However, the /api/submit_score endpoint is protected by:
A per-user request deduplication lock
A rate‑limit
A server‑side token validation mechanism
A timed delay (15–55 ms)
A SHA256‑based request token using a secret

The goal is to bypass the token protection, automate score submissions, and reach 20 valid submissions to get the flag.

Step 1 — Understanding the Token Mechanism

Inside /api/submit_score, before accepting a score, the server checks:

expected_token = generate_request_token(user['id'], score, int(now // 1))
if token != expected_token:
    return invalid_token


And the token is generated using:

secret = "x9k#mPv!q2"
data = f"{user_id}{score}{timestamp_sec}{secret}"
sha256(data)[:16]


Important observations:

The secret is hardcoded in the source code

→ meaning we can generate valid tokens ourselves.

The timestamp is integer seconds from the server's clock

→ If our clock is out of sync, tokens will be invalid.

Step 2 — Extracting the Server Time

There is a hidden endpoint:

/api/debug


It returns:

{"status": "operational", "time": 1732994602.9988}


We can use it to:
Know the server time
Sync submissions to the exact second
Generate valid tokens every time

Step 3 — Designing the Exploit

We need:
20+ valid submissions
Each with a correct token
All synchronized to avoid server delays overwriting timestamps
All bypassing the request_lock mechanism



def wait_for_fresh_second():
    t = get_server_time()
    while get_server_time() == t:
        time.sleep(0.005)
    return get_server_time()


This forces each score submission to occur in a new second, ensuring:

✔️ timestamp_sec matches the server's expectation
✔️ SHA256 token always correct
✔️ No collisions with the per-user request lock

Each request:

Waits for a clean new second
Generates the right SHA256 token
Submits a valid score
Repeats until the flag is returned

Step 4 — Running the Attack
The whole exploitation script is under exploit.py

🏁 Final Flag
CM{6fc6a17d2aa96fa2ada2b02553b2a0ee}
