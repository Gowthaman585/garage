import re

def check_valid(log):
    if re.search("sshd",log):
        if re.search("Received disconnect from",log):
            return "received_disconn_check"
        elif re.search("Disconnected",log):
            return "disconn"
        elif re.search("Accepted",log):
            return "conn"
        elif re.search("maximum authentication",log):
            return "max_authentication_attempts"
        elif re.search("session opened",log):
            return "session_open"
        elif re.search("session closed",log):
            return "session_closed"
        elif re.search("Too many authentication failures",log):
            return "multiple_authentication_failure"
        elif re.search("Bad protocol",log):
            return "bad_protocol"
        elif re.search("Invalid user",log):
            return "invalid_user"
        elif re.search("Did not receive identification string ",log):
            return "not_received_auth_string"
        elif re.search("Failed password",log):
            return "failed_password"
        elif re.search("Connection closed by",log):
            return "conn_close"
        elif re.search("Connection reset by",log):
            return "conn_reset"
        elif re.search("authentication failure",log):
            return "auth_failure"
    else:
        pass
