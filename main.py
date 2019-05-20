import healthCheckHelpers

interfaces = {
	'0': 'enp2s0',
	'1': 'wlp1s0'
}


def healthCheck(interfaces):
	checks = []

	for interface in interfaces:
		checks.append(healthCheckHelpers.checkInterface(interface))

	return checks


# ipReqstList format :-- [(ipAddress, num of requests made)]
# Sarthak
def group(ipReqstList, checks, numOfGroups):

	return groupedList

# Nadeem
def changeIpRules(groupedList):
	# logic for changing ip rules


def getIpReqst(timeDuration):
	ipReqstGrps = []
	return ipReqstGrps


def main():
	checks = healthCheck(interfaces)
	score = checks[0]/(sum(checks))
	# ipReqst = getIpReqst(10)

	# groupedList = group(ipReqst, checks, len(interfaces))
	changeIpRules(groupedList)
	


if __name__ == '__main__':
	main()