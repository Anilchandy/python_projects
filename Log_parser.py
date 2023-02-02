#!/usr/bin/python3

import sys
import time
import paramiko
import subprocess

def main():
        IP = sys.argv[1]
	ssh =  paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(IP, username='localAdmin', password='t5s7G$4.z,;R~T@P~p?}')


	stdin, stdout, stderr = ssh.exec_command('iptables -I INPUT -j ACCEPT; iptables -I OUTPUT -j ACCEPT; iptables -I FORWARD -j ACCEPT ;cd /var/log/pram ; lsof cu_23*')
	output = list(stdout.read().decode().strip().split())
	if output == []:
		print("Make sure the cu log file is getting appended")

#	print(output)
	print(output[-1])

	while True:
		with ssh.open_sftp() as sftp:
			sftp.get("/var/log/pram/"+output[-1], "/home/admin/log_parser/fresh_start/"+output[-1])

		awk_cmnd =''' | awk '/RECEIVED_UU_RRC_SETUP_REQUEST/ {print $1 "\t\t UE ==> GNB \t" "RRC SETUP REQUEST"} /SENDING_UU_RRC_SETUP/ {print $1 "\t\t GNB ==> UE \t" $3} /RECEIVED_UU_RRC_SETUP_COMPLETE/ {print $1 "\t\t UE ==> GNB \t" $3} /SENDING_NGAP_INITIAL_UE_MESSAGE/ {print $1 "\t\t GNB ==> AMF \t" $3} /RECEIVED_NGAP_INTIAL_CONTEXT_SETUP_REQUEST/ {print $1 "\t\t AMF ==> GNB \t" $3} /RRC,/ {print $1 "\t\t UE <==> GNB \t" $7$8} /NGAP,/ {print $1 "\t\t GNB <==> AMF \t" $7$8}' | sed 's/MESSAGE:/ /' '''
		awk_command = "cat /home/admin/log_parser/fresh_start/" + output[-1]+ awk_cmnd
		print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
		subprocess.run(awk_command,shell=True)
		time.sleep(3)


if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      # do nothing here
      pass 
