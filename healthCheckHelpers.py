import os

ByteMultiplier = {
	"K": 1024,
	"M": 1024*1024,
	"G": 1024*1024*1024
}

# data format :-- Totalsendrate:3.36KB3.36KB3.36KB
def sendAndRecParser(data):
	val = data.split(':')[1].split('B')[0]
	mul = 1
	if(val[-1].isalpha()):
		mul = ByteMultiplier[val[-1]]

	if(mul != 1):
		val = float(val[:-1])*mul
	else:
		val = float(val)

	return val


def sendAndRecCheck(interface):
	command = os.popen('sudo iftop -B -t -L 0 -s 1 -i ' + interface)
	line = command.readlines()
	if(len(line)):
		sendDataLine = line[-8]
		recDataLine = line[-7]

		send = ""
		rec = ""

		for x in sendDataLine:
			if(x!=" "):
				send += x

		for x in recDataLine:
			if(x!=" "):
				rec += x

		return sendAndRecParser(send),sendAndRecParser(rec)
	return 0,0

def checkInterface(interface):
	send,rec = sendAndRecCheck(interface)
	aggrInterfaceScore = send + rec + 1e-9
	return aggrInterfaceScore