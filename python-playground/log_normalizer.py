
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
            month_and_date = parts[0] +" "+ parts[1].lstrip('0')+" "+parts[2]
            # saving the remaining parts of log to further finding out the ip and username
            ip_and_username_part = parts[3]
            # returning both the variable to next level analysis
            yield month_and_date , ip_and_username_part


def split_ip_username():

    # Using the dictinary to map the ip along with the date to know at which are all the date the ip is used
    ip_month_date = {}
    # Using the variable to find the odd different sshd logs
    corrupted_or_suspic_log_count = 0

    # Calling the splitting_month_date_rem() to get the month and date along with the ip and username parts
    for month_date , user_ip in timestamp_rem():
        # getting the start and end index of ip part form hte user_ip string
        start_index = user_ip.find("from ")+5
        end_index = user_ip.find(" ",start_index)

        if start_index == -1 or end_index== -1:
            corrupted_or_suspic_log_count = corrupted_or_suspic_log_count + 1
        else:
            # the ip is sliced successfully
            ip = user_ip[start_index:end_index]
        

        # reusing the start_index and end_index variable to find out the username
        start_index = user_ip.find("for ")+4
        end_index = user_ip.find(" ",start_index)

        # Same condition to check valid sshd log
        if start_index == -1 or end_index == -1:
            corrupted_or_suspic_log_count = corrupted_or_suspic_log_count + 1
        else:
            username = user_ip[start_index:end_index]
    # Temperory line to check the working
    return corrupted_or_suspic_log_count

l = split_ip_username()
print(l)
