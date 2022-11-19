import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

enqueueString = "/NodeList/1/DeviceList/1/$ns3::PointToPointNetDevice/TxQueue/Enqueue"
dequeueString = "/NodeList/1/DeviceList/1/$ns3::PointToPointNetDevice/TxQueue/Dequeue"

enqueueValues = []
dequeueValues = []

file = open("tcp-example.tr","r+")
lines = file.readlines()
file.close()

for line in lines:
    tmpLineSplit = line.split(" ")
    if tmpLineSplit[2] == enqueueString and tmpLineSplit[0] == '+':
        newEntry = (float(tmpLineSplit[1]),int(tmpLineSplit[36].split("=")[1]))
        enqueueValues.append(newEntry)
    if tmpLineSplit[2] == dequeueString and tmpLineSplit[0] == '-':
        newEntry = (float(tmpLineSplit[1]),int(tmpLineSplit[36].split("=")[1]))
        dequeueValues.append(newEntry)

finalQueueVal = []

for i in range(0,len(enqueueValues)):
    if enqueueValues[i][1] == dequeueValues[i][1]:
        finalQueueVal.append((enqueueValues[i][1],enqueueValues[i][0],dequeueValues[i][0],abs(dequeueValues[i][0]-enqueueValues[i][0])))

x_vals = []
y_vals = []

for val in finalQueueVal:
    x_vals.append(val[2])
    y_vals.append(val[3])

rc('axes', linewidth=1)
rc('font', weight='bold')

# plt.scatter(x_vals,y_vals,marker = "*",color = "purple")
plt.plot(x_vals,y_vals,color= "red")
plt.xlabel("Time (second)",fontsize=14.0, fontweight='bold')
plt.ylabel("Queuing Delay",fontsize=14.0, fontweight='bold')
plt.show()




