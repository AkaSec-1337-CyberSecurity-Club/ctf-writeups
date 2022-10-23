## Zabomb

Description : You received a suspicious file from the k3rn3l4rmy hacking group, the title says ‘Not a Zip Bomb, Please Open’, you decide NOT to open it and instead try to reverse it. It is recommended that you do NOT open this, it will fill your entire disk.

First of all we google the definition of "zip bomb"

Definition : A zip bomb, also known as a decompression bomb or zip of death is a malicious archive file designed to crash or render useless the program or system reading it. It is often employed to disable antivirus software, in order to create an opening for more traditional malware.

Steps i did to solve the challenge :
	1. I uploaded the zip file in a vps.
	2. Unzip it with "unzip -l" to list archive files.
	3. look at the result.
	4. unzip the file even if it will take a long time.
	5. look at the strings unside the file with the smallest size between the 65k files unziped.

flag{w0w_c0mpres51on_&_d3comp53ssi0N_!s_s0_c3wl_ju5t_d0n7_gO_b0OM}

