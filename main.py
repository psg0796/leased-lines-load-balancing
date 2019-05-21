import utils
import os
import time

def healthCheck(interfaces):
	checks = []

	for interface in interfaces:
		checks.append(utils.checkInterface(interface))

	return checks

def changeIpRules(c1, c2):
	utils.get_update_rule(c1, c2)

def main():
	shouldStartScript = input("Please check and set the environment variables in file define_variable.sh and source the file as well as initiallize the routing rules using command 'source ./define_variable.sh && ./initialize.sh' and press 1 to continue else press any number to exit ?\n")
	if(shouldStartScript == '1'):
		interfaces = [os.environ['IF1'], os.environ['IF2']]
		print(interfaces)
		#checks = healthCheck(interfaces)
		#changeIpRules(checks[0], checks[1])
	else:
		exit()

if __name__ == '__main__':
	main()
