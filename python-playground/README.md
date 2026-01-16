# ======================================================================================
					MINI-LOG TOOL
# ======================================================================================

The "mini-log.py" is micro log analyzer tool which helps to instantly find out 
presence of any brute force attacks in your ssh-server

This tool gives a numeric snapshot about the login attempts  their failure and success.
which helps SOC analyst quicky smell about any brute-force login attempts or major login types password or key's.

This tool uses simple python program to find out the mathcing tags in  the log lines in-order
to find out the login ssh-log lines

# =======================================================================================
						DISCLAIMER
# =======================================================================================
	* Use auth.log or any sample log file that must includes the log lines of sshd 
	* This tool is  built to work only on the sshd log lines
# ---------------------------------------------------------------------------------------

In this repository as you can see two log file are taken for testing purpose
	* sample.log
		this log file is a copy of my personal server log , i just took some copy of it.
	* auth.log
		this is huge popular lof file , i downloaded from the internet which is a popular log file for testing detection of brute force attacks
# ========================================+++++==========================================

As the sample.log file is my personal server logs , so there is no chance for detecting brute force attempts

you can see the difference completely by comaparing the two results of these two log file

# sample.log
!["sample.log file test results"](images/sample.log)
As you can see almost all log attempts are successful and there is minimal level failed logins attempts 
so by we can conclude it is legitimate log history

# auth.log
!["auth.log file test results"](images/auth.log)
The total number of failed logins is at peak and most of the brute force attacks is always on passwords.
the high number failed password confirmly indicates the brute force attempt for ssh login via password.
# ========================================================================================


