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

print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck")

							elif opcion2 == "2":
								cmd = os.system("apt-get install ace-voip")

							elif opcion2 == "3":
								cmd = os.system("apt-get install amap")
							elif opcion2 == "4":
								cmd = os.system("apt-get install automater")
							elif opcion2 == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif opcion2 == "6":
								cmd = os.system("apt-get install braa")
							elif opcion2 == "7":
								cmd = os.system("apt-get install casefile")
							elif opcion2 == "8":
								cmd = os.system("apt-get install cdpsnarf")
							elif opcion2 == "9":
								cmd = os.system("apt-get install cisco-torch")
							elif opcion2 == "10":
								cmd = os.system("apt-get install cookie-cadger")
							elif opcion2 == "11":
								cmd = os.system("apt-get install copy-router-config")
							elif opcion2 == "12":
								cmd = os.system("apt-get install dmitry")
							elif opcion2 == "13":
								cmd = os.system("apt-get install dnmap")
							elif opcion2 == "14":
								cmd = os.system("apt-get install dnsenum")
							elif opcion2 == "15":
								cmd = os.system("apt-get install dnsmap")
							elif opcion2 == "16":
								cmd = os.system("apt-get install dnsrecon")
							elif opcion2 == "17":
								cmd = os.system("apt-get install dnstracer")
							elif opcion2 == "18":
								cmd = os.system("apt-get install dnswalk")
							elif opcion2 == "19":
								cmd = os.system("apt-get install dotdotpwn")
							elif opcion2 == "20":
								cmd = os.system("apt-get install enum4linux")
							elif opcion2 == "21":
								cmd = os.system("apt-get install enumiax")
							elif opcion2 == "22":
								cmd = os.system("apt-get install exploitdb")
							elif opcion2 == "23":
								cmd = os.system("apt-get install fierce")
							elif opcion2 == "24":
								cmd = os.system("apt-get install firewalk")
							elif opcion2 == "25":
								cmd = os.system("apt-get install fragroute")
							elif opcion2 == "26":
								cmd = os.system("apt-get install fragrouter")
							elif opcion2 == "27":
								cmd = os.system("apt-get install ghost-phisher")
							elif opcion2 == "28":
								cmd = os.system("apt-get install golismero")
							elif opcion2 == "29":
								cmd = os.system("apt-get install goofile")
							elif opcion2 == "30":
								cmd = os.system("apt-get install lbd")
							elif opcion2 == "31":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "32":
								cmd = os.system("apt-get install masscan")
							elif opcion2 == "33":
								cmd = os.system("apt-get install metagoofil")
							elif opcion2 == "34":
								cmd = os.system("apt-get install miranda")
							elif opcion2 == "35":
								cmd = os.system("apt-get install nmap")
							elif opcion2 == "36":
								print ('ntop is unavailable')
							elif opcion2 == "37":
								cmd = os.system("apt-get install p0f")
							elif opcion2 == "38":
								cmd = os.system("apt-get install parsero")
							elif opcion2 == "39":
								cmd = os.system("apt-get install recon-ng")
							elif opcion2 == "40":
								cmd = os.system("apt-get install set")
							elif opcion2 == "41":
								cmd = os.system("apt-get install smtp-user-enum")
							elif opcion2 == "42":
								cmd = os.system("apt-get install snmpcheck")
							elif opcion2 == "43":
								cmd = os.system("apt-get install sslcaudit")
							elif opcion2 == "44":
								cmd = os.system("apt-get install sslsplit")
							elif opcion2 == "45":
								cmd = os.system("apt-get install sslstrip")
							elif opcion2 == "46":
								cmd = os.system("apt-get install sslyze")
							elif opcion2 == "47":
								cmd = os.system("apt-get install thc-ipv6")
							elif opcion2 == "48":
								cmd = os.system("apt-get install theharvester")
							elif opcion2 == "49":
								cmd = os.system("apt-get install tlssled")
							elif opcion2 == "50":
								cmd = os.system("apt-get install twofi")
							elif opcion2 == "51":
								cmd = os.system("apt-get install urlcrazy")
							elif opcion2 == "52":
								cmd = os.system("apt-get install wireshark")
							elif opcion2 == "53":
								cmd = os.system("apt-get install wol-e")
							elif opcion2 == "54":
								cmd = os.system("apt-get install xplico")
							elif opcion2 == "55":
								cmd = os.system("apt-get install ismtp")
							elif opcion2 == "56":
								cmd = os.system("apt-get install intrace")
							elif opcion2 == "57":
								cmd = os.system("apt-get install hping3")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")



						while opcion1 == "2":
							print ('''
\033[1;36m=+[ Vulnerability Analysis\033[1;m
