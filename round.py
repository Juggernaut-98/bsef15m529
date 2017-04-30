from collections import deque
def add(time,que=deque([]),process={},key=[],io=[],enter=[]):
	i=0
	count=0	
	x=len(enter)
	while i<x:
		if process.get(enter[i])[0]<=time:
			que.append(enter[i])
			count=count+1
			enter[i]=-1
		i=i+1
	while count>0:
		enter.remove(-1)
		count=count-1
	i=0
	x=len(io)
	while i<x:
		if process.get(io[i])[3]<=time:
			que.append(io[i])
			count=count+1
			io[i]=-1
		i=i+1
	while count>0:
		io.remove(-1)
		count=count-1

def appending(time,key,que=[]):
	i=0
	while(i<time):
		que.append(key)
		i=i+1
	return
#procss=name:[a.t,bt,r.t,nextquetime,i/oremainingtime,timeforruning]
process={1:[0,7,7,0,2,3],2:[2,4,4,2,-1,3],3:[3,3,3,3,2,3],4:[5,5,5,5,-1,3],5:[7,6,6,7,2,3]}
key=[1,2,3,4,5]
enter=[1,2,3,4,5]
iotime=2
n=5
ts=3
wt=5
RQ=[]
io=[]
Ready=deque([])
time=0
while n>0:
	add(time,Ready,process,key,io,enter)
	if Ready:
		element=Ready.popleft()	
		if process.get(element)[4]==-1:
			if process.get(element)[2]<ts:
				appending(process.get(element)[2],element,RQ)
				time=time+process.get(element)[2]
				process.get(element)[2]=0
				print 'process= ',element,' turnaround time=',time-process.get(element)[0]
				n=n-1
			else:
				time=time+ts
				appending(ts,element,RQ)
				process.get(element)[2]=process.get(element)[2]-ts
				add(time,Ready,process,key,io,enter)
				Ready.append(element)
		else:
			if process.get(element)[2]<=process.get(element)[4]:
				time=time+process.get(element)[2]
				appending(process.get(element)[2],element,RQ)
				process.get(element)[2]=0
				print 'process= ',element,' turnaround time=',time-process.get(element)[0]
				n=n-1
			elif process.get(element)[5]<process.get(element)[4]:
				appending(process.get(element)[5],element,RQ)
				process.get(element)[4]=process.get(element)[4]-process.get(element)[5]
				process.get(element)[2]=process.get(element)[2]-process.get(element)[5]
				time=time+process.get(element)[4]
				process.get(element)[5]=ts
				add(time,Ready,process,key,io,enter)
				Ready.append(element)
			elif process.get(element)[5]>=process.get(element)[4]:
				time=time+process.get(element)[4]
				appending(process.get(element)[4],element,RQ)
				process.get(element)[2]=process.get(element)[2]-process.get(element)[4]
				process.get(element)[5]=process.get(element)[5]-process.get(element)[4]
				io.append(element)
				process.get(element)[4]=iotime
				process.get(element)[3]=time+wt
	else:
		RQ.append(-1)
		time=time+1
print RQ
			
	
