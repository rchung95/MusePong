
import collections
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
		return dataAvg>bias?(dataAvg-bias)/right_scale : (bias-dataAvg)/left_scale