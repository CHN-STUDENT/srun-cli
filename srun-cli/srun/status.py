#!/usr/bin/python
# -*- coding: utf-8 -*-
#!Design by CHN-STUDENT

from urllib import request

def GetStatus():
	req = request.Request('http://172.16.154.130/cgi-bin/rad_user_info')
	with request.urlopen(req) as f:
		return f.read().decode('utf-8') #Byte to string

def CheckStatus(data):	
		if (data == 'not_online'): #if user is not online
			return 0
		else:		#if user is online
			output='''
You are already online.
#########################
#  Here are your info:  #
#########################
Username: '''	
			infolist=[
						data.split(',')[0], #username
						str(float(data.split(',')[6])/1073741824), #data
						str(int(int(data.split(',')[7])/3600)),#Hours
						str(int(int(data.split(',')[7])/60%60)),#Mintues
						str(int(int(data.split(',')[7])%60)),#Seconds
						data.split(',')[8] #IP
					 ]
			output=output+infolist[0]+'\nData: '+infolist[1]+' GB\nTime: '+infolist[2]+'  Hours  '+infolist[3]	\
					+'  Mintues  '+infolist[4]+'  Seconds\nIP: '+infolist[5]+'\n#########################'
			print(output)
			return 1


if __name__ == '__main__':
	response = GetStatus()
	CheckStatus(response)