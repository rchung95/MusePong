import sys
#lsimport collections

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
			return (dataAvg-self.bias)/self.right_scale
		else:
			return (self.bias-dataAvg)/self.left_scale

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

def sendData():
	for line in sys.stdin:
		data_tmp = line.split()
		if(len(data_tmp >=5 and data_tmp[1] == '/muse/acc')):
			to_send = usr.mapMove(data_tmp[XCOORD])
			print(str(to_send)

	


inp = input()
if int(inp)==1:
	print("input 1")
	getBias()

