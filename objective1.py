import random

x=10
y=10
intervalOfStations=2
noOfChargingStations=x*y//intervalOfStations**2
location_queue=[[2,3,5],[4,4,5],[5,3,1],[7,1,6],[6,5,3],[-3,4,7],[5,5,1],[-4,4,7]]
origin=[0,0]
horiz_highway=[0,3]
vert_highway=[0,1,2]
int_min_speed=20
int_max_speed=40
high_min_speed=60
high_max_speed=80
min_queue=0
max_queue=10
chargingTimePerCar=0.1

################################################################################################################


def queues():
    ans=[]
    for i in range(noOfChargingStations):
        ans.append(random.randrange(min_queue,max_queue))
    return ans

def makeStations(x,y):
    ans=[]
    for i in range(0,x,2):
        for j in range(0,y,2):
            ans.append([i,j])
    return ans


def distanceBetweenAB(A,B):
    hor_dis=abs(A[0]-B[0])
    ver_dis=abs(A[1]-B[1])
    return hor_dis + ver_dis


def getAllDistances(o,l):
    ans=[]
    for i in l:
        d=distanceBetweenAB(o,i)
        ans.append(d)
    return ans

def getWaitingTime(q):
    ans=[]
    for i in q:
        t=i*chargingTimePerCar
        ans.append(t)
    return ans

def ishighway(hh,vh,x):
    if x[0] in hh or x[1] in vh:
        return True
    return False

def speedToTravel(hh,vh,o,dst):
    ans=[]
    for i in dst:
        ans.append(random.randrange(int_min_speed,int_max_speed))
    return ans

def timeToTravel(td,ts):
    ans=[]
    for i in range(noOfChargingStations):
        tt=td[i]/ts[i]
        ans.append(tt)
    return ans


def getTotalTime(wt,tt):
    ans=[]
    for i in range(noOfChargingStations):
        ans.append(wt[i]+tt[i])
    return ans


def getProperTime(t):
    ans=[]
    for i in t:
        hr=int(i//1)
        min=int((i%1)*60)
        tmp=str(hr)+" hours "+str(min)+" minutes"
        ans.append(tmp)
    return ans

################################################################################################################

stations=makeStations(x,y)
queue=queues()
travelDistances=getAllDistances(origin,stations)
waitingTimes=getWaitingTime(queue)
travelSpeeds=speedToTravel(horiz_highway,vert_highway,origin,stations)
travelTime=timeToTravel(travelDistances,travelSpeeds)
totalTime=getTotalTime(waitingTimes,travelTime)


print("All Charging Stations: ",stations)
print()
#print("Number of Vehicles at each CS: ",queue)
print(totalTime)
print()
print(getProperTime(totalTime))

