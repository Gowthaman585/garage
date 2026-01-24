
# The function which passes the log line one by one without access the complete log file at starting time
def pass_sshd_log():
    
    # start with try to handle the file-not-found errors
    try:
        with open("auth.log",'r',buffering = 8192) as file:
            for line in file:
                # r.strip is used here to remove all the trailing new line strings
                line = line.rstrip()
                if 'sshd[' in line:
                    # yield is used to return the line without quiting the complete program
                     yield line
    except FileNotFoundError:
        print("No such a File")
 

def timestamp_rem():
    
    for log in pass_sshd_log():
        # The .split(maxsplit=2) is a fastest way to split the string into two parts
        # Because after splitinf the first two part it take the remaining whole into next part
        parts = log.split(maxsplit=3)
        
        # Entry check that log is properly splitted corrupted logs need not to be processed
        if len(parts) == 4:
            # parts[0] is month parts[1] is date
            # The .lstrip is used to remove the trailing zeros from a string 
            timestamp = parts[0] +" "+ parts[1].lstrip('0')+" "+parts[2]
            # saving the remaining parts of log to further finding out the ip and username
            message = parts[3]
            # returning both the variable to next level analysis
            yield timestamp , message


def suspicious_logs():
    
    for timestamp , message in timestamp_rem():
        if "error:" in message:
            pass



