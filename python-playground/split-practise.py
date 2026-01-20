print("===== Practising next level log analysis =====")

# Sample log line for practising
line = "Mar 27 13:08:09 ip-10-77-20-248 sshd[1361]: Accepted publickey for ubuntu from 85.245.107.41 port 54259 ssh2"

# Splitting the log line into two parts (left-right)
# Left part has the details about the timestamps,hostname and processid
# Right part contains the actual message of this log along with the host ip, port and protocol name
part = line.split(": ",1)
left_part = part[0]
right_part = part[1]

# Spliting the left_part to obtain actual targets
# holder used to help in separating each string in the leftpart in-order to easy retrive of targets
holder = left_part.split(" ",4)

# Extraction of actual targets
# The timestamp are separted into three string so they need to rejoin into one
timestamp = holder[0]+" "+holder[1]+" "+holder[2]
hostname = holder[3]
process = holder[4]

# Now analysing right part to obtain the host ip and port
# finding starting and ending index of ip address
start_index_ip = right_part.find("from ")+5
end_index_ip = right_part.find(" ",start_index_ip)

# Using string slicing to exactly retive the ip address
ip_addr = right_part[start_index_ip:end_index_ip]

# Finding start and end index of port number
start_index_port = right_part.find("port ")+5
end_index_port = right_part.find(" ",start_index_port)

# Using string slicing to extract the port number
port_number = right_part[start_index_port:end_index_port]

# Finding start and end index of username 
start_index_username = right_part.find("for ")+4
end_index_username = right_part.find(" ",start_index_username)

# String slicing to retrive the username
username = right_part[start_index_username:end_index_username]

# ========= Printing all the retrived data to verify ==========
print("======== verification ========")
print(f"Timestamp   :   {timestamp}")
print(f"Hostname    :   {hostname}")
print(f"Process-ID  :   {process}")
print(f"Ip-address  :   {ip_addr}")
print(f"Port-number :   {port_number}")
print(f"User-Name   :   {username}")
