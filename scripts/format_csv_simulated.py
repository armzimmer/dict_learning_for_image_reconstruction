import sys
import csv
csv.field_size_limit(sys.maxsize)

timestamp = []
x = []
y = []
pol = []

sec = 0

cntr=0
with open('out-cam0-events.csv') as csvfile:
    print("opened file!")
    event_file = csv.reader(csvfile, delimiter='\n')
    next(event_file)
    for row in event_file:
        #print(".")
        if cntr >= 49:
            break
        if len(row) == 0:
            continue; # while writing, an additional alternative empty row is written in the excel. so skippping
        if 'x' in row[0]:
            #print(row[0][row[0].rfind('x')+3:])
            x.append(int(float(row[0][row[0].rfind('x')+3:])))
        if 'y' == row[0][0]:
            #print(row[0][row[0].rfind('y')+3:])
            y.append(int(float(row[0][row[0].rfind('y')+3:])))
        if 'secs' in row[0] and not 'nsecs' in row[0]:
            #print(row[0][row[0].rfind('secs')+6:])
            sec = int(float(row[0][row[0].rfind('secs')+6:]))
        if 'nsecs' in row[0]:
            #print(str(sec)+'.'+str(int(row[0][row[0].rfind('nsecs')+7:])).zfill(9))
            timestamp.append(float(str(sec)+'.'+str(int(row[0][row[0].rfind('nsecs')+7:])).zfill(9)))
        if 'polarity' in row[0]:
            #print(row[0])
            #print(row[0].split(' ')[1][:-1])
            if(row[0].split(' ')[1][:-1] == 'True' or row[0].split(' ')[1][:-1] == 'True]'):
                pol.append(int(1))
            elif(row[0].split(' ')[1][:-1] == 'False' or row[0].split(' ')[1][:-1] == 'False]'):
                pol.append(int(0))
            else:
                print(row[0].split(' ')[1][:-1] )
                print("Something went wrong with reading event file!\n")

print("x:", len(x))
print("y:", len(y))
print("timestamp:", len(timestamp))
print("polarity:", len(pol))

import pickle

my_dict= {'x': x, 'y': y, 'timestamp': timestamp, 'pol': pol}
with open("sim_berlinale.pkl", "wb") as pklfile:
    pickle.dump(my_dict, pklfile)

#import pickle
#with open("sim_events.pkl", "rb") as pklfile:
#    events = pickle.load(pklfile)
