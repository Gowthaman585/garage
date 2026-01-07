import re


# Opening the file in read mode to analyze
with open("copy.txt",'r') as file:
	lines = file.readlines()

# increamenting variable
ssh_count = 0

# snippet to count the ssh-log lines particularly
for i in lines:
	if re.search("sshd",i):
		ssh_count = ssh_count + 1

# displaying total number of ssh log lines
print(f" Total amount ssh log lines {ssh_count}")

