CTF Write-up — Caption Studio

Category: Rhythm Revolution
Points: 160
Author: sn0_0wyy

🔍 Challenge Summary

The challenge description hints at:

"Z10UDI gave you something right??"

When i clicked on the link provided in the chal it took me to a webpage i tried to log in and it asked for a secret key so i input "Pr0ducti0n_B4ckUP_K3Y!" this was recovered in the previous challenge. you are taken to another page which says:

“FFmpeg will see this exactly as you type it. No filters, no guard rails.”

There is an input box labelled Caption text.
The backend takes whatever you write and directly embeds it into an FFmpeg filtergraph.
No sanitization → this is a classic FFmpeg filter injection → Local File Read (LFR) challenge.

You are logged in as:studio_admin

The goal is to craft a payload that forces FFmpeg to load a file from the server, typically containing the flag.

🎯 Exploitation Strategy

FFmpeg has a filter called movie= that loads ANY file readable by the server.

The challenge says the flag is stored at /flag/flag.txt so 