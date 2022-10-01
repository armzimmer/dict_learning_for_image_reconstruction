import csv

file = open("poster_6dof.csv", "r")
data_old = list(csv.reader(file, delimiter=","))
file.close()

data = data_old[:40]

#data[0] = ['# timestamp', ' x', ' y', ' z', ' qx', ' qy', ' qz', ' qw']

for i in range(39):
  data[i+1][0] = i*250000000 # t
#  data[i+1][1] = -0.3+ i*0.009 # x
  data[i+1][1] = -0.35+ i*0.009 # x
  data[i+1][2] = 0.3- i*0.009 # y
  data[i+1][3] = -0.65 # z
  data[i+1][4] = 0 # qx
  data[i+1][5] = 0 # qy
  data[i+1][6] = 0 # qz
  data[i+1][7] = 1 # qw

with open("my_traj_new.csv", "w") as f:
  wri = csv.writer(f)
  wri.writerows(data)
