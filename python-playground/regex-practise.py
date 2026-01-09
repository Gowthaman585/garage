import re

# Opening the file in read mode to analyze
with open("copy.txt",'r') as file:
	lines = file.readlines()

# increamenting variable for counting successful ssh-login attemnpts
ssh_pass = 0

# incrementing variable for failed ssh-login attempts
ssh_fail = 0

# incrementing variable for no of successful disconnections
ssh_disc = 0

# snippet to count the ssh-log lines particularly
for i in lines:
	if re.search("sshd",i):
		if re.search("Accepted publickey",i) or re.search("Accepted password",i):
			ssh_pass = ssh_pass + 1
		if re.search("Failed password",i):
			ssh_fail = ssh_fail + 1
		if re.search("Disconnected from",i):
			ssh_disc = ssh_disc + 1

# displaying  the detials for ssh-login event details
print(f"Total no of  successful ssh-login attempts : {ssh_pass}")
print(f"Total no of failed ssh-login attempts : {ssh_fail}")
print(f"Total no of successful ssh-disconnection's : {ssh_disc}")
