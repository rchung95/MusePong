import sys



	########################### Prompt the user to calibrate: stand ##################
data_stand = []
data_tmp = []
count= 2
for place, line in enumerate(sys.stdin):
	if(place<10):
		continue
	
	data_tmp = line.split()
	#print(data_tmp)
	
	
	if(len(data_tmp)>=6 and data_tmp[1] == '/muse/acc'):
		data_stand.append(data_tmp[3])

	#data_tmp = input from Muse
print data_stand

print str(len(data_stand))

	##################### Prompt the user to calibrate: move head right/left ##################
	#User user = new User(data_cal, bias);

	##################### Start the game  ##################