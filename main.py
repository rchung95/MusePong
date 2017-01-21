import csv
import setup
import sys

if __name__=="main":

	########################### Prompt the user to calibrate: stand ##################
	data_stand = []
	data_tmp = []
	count = 0
	while(count < 10000):   # While standing
		data_tmp = sys.stdin
		if(data_tmp[1] == ' /muse/acc'):
			data_stand.append(data_tmp[4])
	#data_tmp = input from Muse
	print data_stand
	bias = sum(data_stand)/len(data_stand)
	##################### Prompt the user to calibrate: move head right/left ##################
	data_cal = []
	if(data_tmp[1] == ' /muse/acc'):
		data_cal.append(data_tmp[4])

	User user = new User(data_cal, bias);

	##################### Start the game  ##################