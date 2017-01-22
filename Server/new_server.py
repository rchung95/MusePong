import fileinput
import time



#read input continously
def read_input():
	while True:
		for line in fileinput.input():
			if len(line.split()) > 2 and line.split()[1] == '/muse/acc':
				return (line.split())


#get position of head (read size number of data)
def get_buffer(size):
	input_holder = []
	fi = fileinput.input()

	for line in fi:
		if (len(input_holder) > size):
			break
		if len(line.split()) > 2 and line.split()[1] == '/muse/acc':
			#print line.split()
			input_holder.append(float(line.split()[3]))

	fi.close()
	return input_holder

#get position of head when tilting left
print("Application Starting...\nCalibrating...\n")
previous_location = get_buffer(200)
current_location = get_buffer(5)


print(sum(previous_location) / 200)
print(sum(current_location) / 5)



#start game
while True:
	fi = fileinput.input()

	for line in fi:
		if len(line.split()) > 2 and line.split()[1] == '/muse/acc':
			#print line.split()
			previous_location.append(float(line.split()[3]))
			previous_location.pop(0)
			current_location.append(float(line.split()[3]))
			current_location.pop(0)
		
		if (sum(current_location)/5 - sum(previous_location)/200 > 100):
			print(1)

		elif (sum(current_location)/5 - sum(previous_location)/200 < -30):
			print(-1)

		else:
			print(0)





# def getRange():
# 	data_calc = []
# 	data_tmp = []
# 	for place, line in enumerate(sys.stdin):
# 		if(place<10):
# 			continue
# 		data_tmp = line.split()
# 		if(len(data_tmp)>=5 and data_tmp[1] == '/muse/acc'):
# 			data_calc.append(data_tmp[XCOORD])
# 		if (len(data_calc) > CALIB_TIME):
# 			break;
# 	return data_calc

#prompt user to calibrate


# print("Application Calibrating...Keep head still\n")
# still = get_still()
# print(still)

# time.sleep(1)
# print("Application Calibrating...move head left\n")
# time.sleep(0.5)
# left = get_still()
# print(left)

# time.sleep(1)
# print("Application Calibrating...move head right\n")
# right = get_still()
# print(right)



#print("hiii")

		



