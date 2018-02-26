#!/usr/bin/env python 

'''
Like "w", but find all processes associated with a TTY (not just 
those registered in wtmp), and reports all users that are running
anything. In particular, unlike "w", this will shows things running 
in detached screens/tmuxen

From Wikipedia, the free encyclipedia
	
	a) utmp, wtmp, btmp and variants such as utmpx, wtmpx and btmpx 
	are files on Unix-like systems that keep track of all logins and logouts to system.
	
	b) glob -- Unix style pathname pattern expansion 

'''


import sys, os, glob, pwd, time 

# Find all TTYs
ttys = {}
for tty in glob.glob("/dev/tty*") + glob.glob("/dev/pts/*"):
	try:
		st = os.stat(tty)
	except EnvironmentError:
		continue
	
# atime is time of last input 
# mtime is time of last output 
# ctime is when it was created 
	ttys[st.st_rdev] = (tty[5:], st, [])

# Find all process and map them to TTYs
notty = {}
uids = set()
for pid in os.listdir("/proc"):
	if not pid.isdigit():
		continue
	pid = int(pid)

	try:
		with open("/proc/%d/stat" % pid, 'r') as statusfile:
			status = statusfile.read()
		with open("/proc/%d/cmdline" % pid, 'r') as cmdlinefile:
			cmdline = cmdlinefile.read()
		st = os.stat("/proc/%d" % pid)
	except EnvironmentError:
		continue 
	uids.add(st.st_uid)

	parts = status.rsplit(") ", 1)[1].split()
	tty_nr = int(parts[4])
	tpgid = int(parts[5])
	if tty_nr == 0 or tpgid == -1:
		# No controlling terminal 
		notty
