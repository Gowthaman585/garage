import re

count = 0

def pass_sshd_log():
    try:
        with open("auth.log",'r') as file:
            for line in file:
                if re.search(r"sshd\[\d+\]", line):
                    yield line
                else:
                    continue
    except FileNotFoundError:
        print("No such a File")

"""
# FOR TESTING PUPROSE 
# PRINTING FIRST 50 LINE OF VALID LOG LINES WHICH CONTAINS THE KEY TERM SSHD[PROCESS_ID] IN THEIR LOG LINE


for log in pass_sshd_log():
    print(log,end="")
    count = count + 1
    if count == 50:
        break 
"""
