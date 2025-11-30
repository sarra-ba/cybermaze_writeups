CTF Write-up — Caption Studio

Category: Rhythm Revolution
Points: 160
Author: sn0_0wyy

🔍 Challenge Summary

The challenge description hints at:

"Z10UDI gave you something right?? Link"
When i clicked on the link provided in the chal it took me to a webpage i tried to log in and it asked for a secret key so i input "Pr0ducti0n_B4ckUP_K3Y!" this was recovered in the previous challenge. you are taken to another page which says he page says:

“FFmpeg will see this exactly as you type it. No filters, no guard rails.”

There is an input box labelled Caption text.
The backend takes whatever you write and directly embeds it into an FFmpeg filtergraph.
No sanitization → this is a classic FFmpeg filter injection → Local File Read (LFR) challenge.

You are logged in as:
This strongly suggests we are interacting with a web service that processes user-supplied media. A common CTF trick is that the backend uses FFmpeg, making it vulnerable to filter injection, arbitrary file read, or command expansion inside FFmpeg filter syntax.

The goal is to craft a payload that forces FFmpeg to load a file from the server, typically containing the flag.

🕵️‍♂️ Recon

Accessing the provided link loads a Caption Studio interface:

you upload a video or an image

you type a "caption" or "effect"

the backend runs FFmpeg with your input

the output is displayed back to you

Trying simple punctuation ([, ], ;, movie=) shows that FFmpeg outputs errors, confirming that:

the input is passed directly into an FFmpeg filter graph

no sanitization is performed

we can inject FFmpeg filter syntax

Example of the backend log:

FFmpeg will see this exactly as you type it.


Perfect — classic FFmpeg injection challenge.

🎯 Exploitation Strategy

FFmpeg has a filter called movie= that loads ANY file readable by the server.

So if the flag is stored at something like: