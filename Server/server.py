import sys
import collections
import socket

CALIB_TIME = 200 #number of samples
XCOORD = 3 # index of x coord

class UserData:
	def __init__(self, dataSet, bias):
		self.bias = bias
		self.right_scale = max(dataSet) - bias
		self.left_scale = bias - min(dataSet)
		self.buffer = collections.deque(maxlen=25)
		print ("new user with bias "+str(self.bias) +" in range "+str(self.scale)+" created!")

	#right most = 1, left most = -1; return a number in between
	def mapMove(self, data):
		"""input: the X-coord read from real time"""
		d.pop()
		d.appendleft(data)
		dataAvg = sum(d)/len(d)
		if dataAvg>self.bias:
			return (dataAvg-self.bias)/right_scale
		else:
			return (self.bias-dataAvg)/left_scale

def getBias():
	data_std = []
	data_tmp = []
	for place, line in enumerate(sys.stdin):
		if(place<10):
			continue
		data_tmp = line.split()
		if(len(data_tmp)>=5 and data_tmp[1] == '/muse/acc'):
			data_std.append(data_tmp[XCOORD])
		if (len(data_std) > CALIB_TIME):
			break;
	
	return sum(data_std)/len(data_std)

def getRange():
	data_calc = []
	data_tmp = []
	for place, line in enumerate(sys.stdin):
		if(place<10):
			continue
		data_tmp = line.split()
		if(len(data_tmp)>=5 and data_tmp[1] == '/muse/acc'):
			data_calc.append(data_tmp[XCOORD])
		if (len(data_calc) > CALIB_TIME):
			break;
	return data_calc
	
###################################### Game Begin###################

########################### Prompt the user to calibrate: stand ##################

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5002)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address
        data_cal = []
        data_stand = []	
        bias = 0
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'data Receive' % data
            if (int(data) == 1): #calibrate to bias
            	print >>sys.stderr, 'getBias started!'
            	bias = getBias() 
            	print >>sys.stderr, 'getBias done!' 
            
            if (int(data) == 2): 
            	print >>sys.stderr, 'getDataSet started!'
            	data_cal = getDataSet()
            	print >>sys.stderr, 'getDataSet done!'

            if (int(data) == 3):
            	print >>sys.stderr, 'Sending muse tilt.'
            	usr = User(data_calc, bias)
            	for line in sys.stdin:
            		print >>sys.stderr, "get line" % line
					data_tmp = line.split()
					if(len(data_tmp >=5 and data_tmp[1] == '/muse/acc')):
						to_send = usr.mapMove(data_tmp[XCOORD])
						print >>sys.stderr, "send single value" % to_send
						connection.sendall(to_send)


    finally:
        # Clean up the connection
        connection.close()





