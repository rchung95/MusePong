import csv
import sys

args = sys.argv

for i in range(1,len(args)):
	with open('Downloads/'+args[i], 'r') as inp, open('cherylmove'+str(i)+'_acc.csv', 'wb') as out:
		writer = csv.writer(out)
		for row in csv.reader(inp):

			if row[1] == " /muse/acc":
				writer.writerow(row)


