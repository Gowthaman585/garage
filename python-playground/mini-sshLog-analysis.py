import re

# Opening the file in read mode to analyze
with open("sample.log",'r') as file:
	lines = file.readlines()

# var for counting successful ssh-login attemnpts
ssh_pass = 0

# var for failed ssh-login attempts
ssh_fail = 0

# var for no of successful disconnections
ssh_disc = 0

# var for particulary counting the events
pubkey = 0
passwd = 0
fpass = 0
fkey = 0
fdrops = 0
# snippet to count the ssh-log lines particularly
for i in lines:
	if re.search("sshd",i):
		if re.search("Accepted publickey",i):
			pubkey = pubkey + 1
		if re.search("Accepted password",i):
			passwd = passwd + 1
		if re.search("Failed password",i):
			fpass = fpass + 1
		if re.search("Failed publickey",i):
			fkey = fkey + 1
		if re.search("Connection closed by authenticating user",i):
			fdrops = fdrops + 1
		if re.search("Disconnected from",i):
			ssh_disc = ssh_disc + 1

# statement for total successful logins
ssh_pass = pubkey + passwd

# statement for total no of failed ssh-login attemps
ssh_fail = fpass + fdrops + fkey

# displaying  the detials for ssh-login event details
print(f"This mini ssh-log analysis tool is most suitable  on auth.log")
print(f"Any other kind of logs may be result in inaccuracy")
print(f"===================== LOG ANALYSIS COMPLETED =====================")
print(f"Total no of ssh-login attempts 		: {ssh_pass + ssh_fail}")
print(f"Total no of successful ssh-logins	: {ssh_pass}")
print(f"	└─ password based logins 	: {passwd}")
print(f"	└─ key based logins 		: {pubkey}")
print(f"Total no of failed ssh-login attempts 	: {ssh_fail}")
print(f"	└─ password failed attempts 	: {fpass}")
print(f"	└─ key failed attempts 		: {fkey}")
print(f"	└─ connection drop out 		: {fdrops}")
print(f"Total no of ssh-logouts : {ssh_disc}")
print(f"Total no of active ssh-sessions : {ssh_pass-ssh_disc}")
