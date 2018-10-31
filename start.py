from MaltegoTransform import *
import sys, os

#create simple name
me = MaltegoTransform()

#Reading entity input (username)
me.parseArguments(sys.argv)
username = me.getVar("text")

#Pass thru and start whatsmyname program
os.system("C:\\Python37\\python.exe web_accounts_list_checker.py -u " + username)

#create counter for final result report
ctr = 0

#Open output file and import found urls to maltego
f = open(username + ".txt", "r")
for line in f:
	me.addEntity("maltego.Domain", line)
	ctr += 1
f.close()

#return new entitys to grahp
me.addUIMessage("completed!!! \nWith " + str(ctr) + "sites found.")
me.returnOutput()
