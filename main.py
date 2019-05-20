import utils
import os

def healthCheck(interfaces):
	checks = []

	for interface in interfaces:
		checks.append(utils.checkInterface(interface))

	return checks

def changeIpRules(c1, c2):
	utils.get_update_rule(c1, c2)

def main():
	shouldStartScript = input("Please check and set the environment variables in file define_variable.sh carefully and press 1 to continue else press any number to exit ?\n")
	if(shouldStartScript == '1'):
		os.popen(". ./define_variable.sh")
		interfaces = [os.environ['IF1'], os.environ['IF2']]
		print(interfaces)
		checks = healthCheck(interfaces)
		changeIpRules(checks[0], checks[1])
	else:
		exit()

if __name__ == '__main__':
	main()