#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess,os,sys
def sendsms(message,number):
	fmodem=subprocess.check_output("sudo mmcli -L", shell=True)
	fcut1="/org/freedesktop/ModemManager1/Modem/"
	pos1=fmodem.find(fcut1)
	pos1+=len(fcut1)
	nmodem=""
	while fmodem[pos1]!=" ":
		nmodem+=fmodem[pos1]
		pos1+=1
	os.system("sudo mmcli -m "+nmodem+" -e")
	fmsg=subprocess.check_output("sudo mmcli -m "+nmodem+" --messaging-create-sms=\"text='"+message+"',number='"+number+"'\"", shell=True)
	fcut2="/org/freedesktop/ModemManager1/SMS/"
	pos2=fmsg.find(fcut2)
	pos2+=len(fcut2)
	nmsg=""
	while fmsg[pos2]!=" ":
		nmsg+=fmsg[pos2]
		pos2+=1
	os.system("sudo mmcli -s "+nmsg+" --send")
r_args=['-m','-n','-help']
sudo = os.geteuid()
if sudo == 0:
	number=""
	message=""
	for arg in range(0,len(sys.argv)):
		if "-" in sys.argv[arg] and sys.argv[arg] not in r_args:
			print "run 'sudo python smsgsm.py -help' in terminal ..."
			break
		if sys.argv[arg-1]=="-m":
			message=sys.argv[arg]
		if sys.argv[arg-1]=="-n":
			number=sys.argv[arg]
		if sys.argv[arg]=="-help":
			print "sudo python smsgsm.py -m 'message text example' -n '6936000000'"
	if len(sys.argv)==1:
		print "run 'sudo python smsgsm.py -help' in terminal ..."
	if message!="" and number!="":
		sendsms(message,number)
else:
	print "Run this script as root !!!"
	print "sudo python smsgsm.py -m 'message text example' -n '6936000000'"
