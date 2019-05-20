import os
import time
ByteMultiplier = {
	"K": 1024,
	"M": 1024*1024,
	"G": 1024*1024*1024
}

def get_update_rule(w1 = 0.5,w2 = 0.5):
	probability = w2//(w1+w2)
	rule = "iptables -t mangle -R PREROUTING 4 -m statistic --mode random --probability %s -j MARK --set-mark 20"%(probability)
	return rule

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

def get_bytes(t, iface='wlp3s0'):
    with open('/sys/class/net/' + iface + '/statistics/' + t + '_bytes', 'r') as f:
        data = f.read()
    return int(data)

def rxtx(interface):
    (tx_prev, rx_prev) = (0, 0)
    while(True):
        tx = get_bytes('tx', interface)
        rx = get_bytes('rx', interface)
        if tx_prev > 0:
            tx_speed = tx - tx_prev
            # print('TX: ', tx_speed, 'bps')

        if rx_prev > 0:
            rx_speed = rx - rx_prev
            # print('RX: ', rx_speed, 'bps')
            break

        time.sleep(1)
    

        tx_prev = tx
        rx_prev = rx
    return tx_speed,rx_speed

def checkInterface(interface):
	send,rec = rxtx(interface)
	aggrInterfaceScore = send + rec + 1e-9
	return aggrInterfaceScore
