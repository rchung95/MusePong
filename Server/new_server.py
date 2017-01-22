#import sys
import fileinput
import time



#read input continously
# def read_input():
# 	while True:
# 		for line in fileinput.input():
# 			if len(line.split()) > 2 and line.split()[1] == '/muse/acc':
# 				return (line.split())


#get position of head (read size number of data)
def get_buffer(size):
	input_holder = []
	fi = fileinput.input()
	print(input_holder)

	for line in fi:
		if (len(input_holder) > size):
			break
		if len(line.split()) > 2 and line.split()[1] == '/muse/acc':
			#print line.split()
			input_holder.append(float(line.split()[5]))

	fi.close()
	return input_holder

#start game
# while True:
def read_data_from_muse(previous_location, current_location):
	fi = fileinput.input()

	for line in fi:
		if len(line.split()) > 2 and line.split()[1] == '/muse/acc':
			print(line.split())
			previous_location.append(float(line.split()[5]))
			previous_location.pop(0)
			current_location.append(float(line.split()[5]))
			current_location.pop(0)
		
		if (sum(current_location)/5 - sum(previous_location)/60 > 80):
			fi.close()
			print(1)
			return 1

		elif (sum(current_location)/5 - sum(previous_location)/60 < -100):
			fi.close()
			print(-1)
			return -1

		else:
			fi.close()
			print(0)
			return 0

	

def go_get_data():
	#get position of head when tilting left
	print("Application Starting...\nCalibrating...\n")
	previous_location = get_buffer(60)
	current_location = get_buffer(5)
	print(previous_location)
	print(current_location)
	while True:
		print(read_data_from_muse(previous_location, current_location))

go_get_data()
# for line in fileinput.input():
# 	print(line)
