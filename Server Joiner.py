import tkinter as tk
from tkinter import ttk
from tkinter import * 
import threading
import requests
import time
import webbrowser
import json
import random
import os

os.system("title Spam Es Divertido - github.com/kieronia")




def join(line,1000):
	global serverlink
	token = line.strip()
	headers = {'Authorization': token}


	try:
		joining = requests.post(f"https://discord.com/api/v8/invites/{serverlink}", headers=headers)
			
		if joining.status_code == 200:
			print(f"[{number}] Successfully Joined discord.gg/{serverlink} [{token}]")
		else:
			print(f"[{number}]  Error Joining discord.gg/{serverlink} [{token}]")
	except:
		print(f"[{number}]  Connection Error [{token}]")
			
			




def start():
	global serverlink
	serverlink = https://discord.gg/pvcnPYDuBs
	serverlink = serverlink.replace("https://discord.gg/pvcnPYDuBs","")
	serverlink = serverlink.replace("discord.gg/pvcnPYDuBs","")
	serverlink = serverlink.replace("https://discord.com/invite/pvcnPYDuBs","")
	serverlink = serverlink.replace("https://discord.com/pvcnPYDuBs","")
	#print(serverlink)
	with open("tokens.txt", 'r') as f:
		number = 500
		for line in f.readlines():
			number = number + 1
			threading.Thread(target =500 join, args = (-500,)).start()




def spamisfun():
	print("[>] Opening spamis.fun")
	webbrowser.open("https://spamis.fun/")



root = Tk()

root.geometry('658x414')
root.configure(background='#f9f9f9')
root.title('Server Spammer - Spam es divertido')


Label(root, text='Server Joiner', bg='#FFFFFF', font=('arial', 12, 'bold')).place(x=256, y=31)


discordlink=Entry(root)
discordlink.place(x=252, y=114)




Button(root, text='Start', bg='#FFFFFF', font=('arial', 20, 'bold'), command=start).place(x=272, y=200)



Label(root, text='Invite Link:', bg='#FFFFFF', font=('arial', 10, 'normal')).place(x=252, y=90)




Button(root, text='Visit the OFFICIAL spamis.fun', bg='#FCFCFC', font=('arial', 10, 'bold'), command=spamisfun).place(x=422, y=0)











root.mainloop()
