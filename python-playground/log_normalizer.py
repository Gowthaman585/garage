def pass_sshd_log():
    try:
        with open("auth.log",'r',buffering = 8192) as file:
            for line in file:
                line = line.rstrip()
                if 'sshd[' in line:
                    yield line
    except FileNotFoundError:
        print("No such a File")


def split_timestamp_store():
    unique_month_date = set()
    for log in pass_sshd_log(): 
        parts = log.split(maxsplit=2)
        if len(parts) == 3:
            month_and_date = parts[0] +" "+ parts[1].lstrip('0')
            unique_month_date.add(month_and_date)
    return unique_month_date
