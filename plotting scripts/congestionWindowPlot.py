import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

filename = "tcp-example.cwnd"
x_vals = []
y_vals = []

file = open(filename,"r+")
lines = file.readlines()
file.close()

tmpLst = []
for line in lines:
    tmp = line.split("\t")
    tmpLst.append((float(tmp[0]),int(tmp[2][:-1])))

tmpLst.sort(key= lambda x:x[0])
for val in tmpLst:
    x_vals.append(val[0])
    y_vals.append(val[1])

rc('axes', linewidth=1)
rc('font', weight='bold')

plt.plot(x_vals,y_vals,color = "darkgreen")
# plt.scatter(x_vals,y_vals,marker = "*",color = "red")
plt.xlabel("Time (second)",fontsize=14.0, fontweight='bold')
plt.ylabel("Congestion Window (MSS)",fontsize=14.0, fontweight='bold')
plt.show()
