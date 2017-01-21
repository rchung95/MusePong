import csv

if __name__=="main":

	########################### Prompt the user to calibrate: stand ##################
	data_stand = []
	#data_tmp = input from Muse
	if(data_tmp[1] == ' /muse/acc'):
		data_stand.append(data_tmp[4])
	bias = sum(data_stand)/len(data_stand)
	##################### Prompt the user to calibrate: move head right/left ##################
	data_cal = []
	if(data_tmp[1] == ' /muse/acc'):
		data_cal.append(data_tmp[4])

	User user = new User(data_cal, bias);

	##################### Start the game  ##################