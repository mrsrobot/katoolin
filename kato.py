#!/usr/bin/python

import os
import sys, traceback

def main():
	try:
		print ('''

 Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem
		''')
		def inicio1():
			while True:
				print ('''
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help
			''')

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")
			
				while opcion0 == "1":
					print ('''
1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file
					''')
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
outfile = "/etc/apt/sources.list"
