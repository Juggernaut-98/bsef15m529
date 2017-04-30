from collections import deque
def appending(time,key,que=[]):
	i=0
	while(i<time):
		que.append(key)
		i=i+1
	return
def add(time,que=deque([]),process={},Q=[]):
	i=0
	count=0
	while i<len(Q):
		if process.get(Q[i])[3]<=time:
			que.append(Q[i])
			Q[i]=-1
			count=count+1
			#print que
		i=i+1
	while count>0:
		Q.remove(-1)
		count=count-1
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
io1=[]
AQ=[]
Ready=deque([])
Aux=deque([])
time=0
while n>0:
	add(time,Ready,process,enter) #for ready que
	add(time,Ready,process,io1)
	add(time,Aux,process,io) #for auxliary que
	if not (Ready or Aux):
		RQ.append(-1)
		time=time+1
	elif Aux:
		element=Aux.popleft()
		if process.get(element)[2]<=process.get(element)[5]:
			#print 'abc'
			time=time+process.get(element)[2]
			appending(process.get(element)[2],element,RQ)
			process.get(element)[2]=0
			n=n-1
			print 'process',element,' turn aroundtime=',time-process.get(element)[0]
		else:
			time=process.get(element)[5]+time
			appending(process.get(element)[5],element,RQ)
			process.get(element)[2]=process.get(element)[2]-process.get(element)[5]
			process.get(element)[4]=process.get(element)[4]-process.get(element)[5]
			process.get(element)[5]=ts
			add(time,Ready,process,enter) #for ready que
			add(time,Ready,process,io1)
			add(time,Aux,process,io)
			Ready.append(element)
	elif Ready:
		#print Ready
		element=Ready.popleft()
		if process.get(element)[4]==-1:
			if process.get(element)[2]<=ts:
				time=time+process.get(element)[2]
				appending(process.get(element)[2],element,RQ)
				process.get(element)[2]=0
				n=n-1
				print 'process',element,' turn aroundtime=',time-process.get(element)[0]
			else:
				time=time+ts
				appending(ts,element,RQ)
				process.get(element)[2]=process.get(element)[2]-ts
				add(time,Ready,process,enter) #for ready que
				add(time,Ready,process,io1)
				add(time,Aux,process,io) #for auxliary que
				Ready.append(element)
		else:
			if process.get(element)[2]<=process.get(element)[4]:
				if process.get(element)[2]<=ts:
					time=time+process.get(element)[2]
					appending(process.get(element)[2],element,RQ)
					process.get(element)[2]=0
					n=n-1
					print 'process',element,' turn aroundtime=',time-process.get(element)[0]
				else:
					time=time+ts
					appending(ts,element,RQ)
					process.get(element)[2]=process.get(element)[2]-ts
					process.get(element)[4]=process.get(element)[4]-ts
					add(time,Ready,process,enter) #for ready que
					add(time,Aux,process,io) #for auxliary que
					Ready.append(element)
			else:
				
				if ts<process.get(element)[4]:				
					time=time+ts
					appending(ts,element,RQ)
					process.get(element)[2]=process.get(element)[2]-ts
					process.get(element)[4]=process.get(element)[4]-ts
					add(time,Ready,process,enter) #for ready que
					add(time,Ready,process,io1)
					add(time,Aux,process,io) #for auxliary que
					Ready.append(element)
				else:
					time=time+process.get(element)[4]
					appending(process.get(element)[4],element,RQ)
					process.get(element)[2]=process.get(element)[2]-process.get(element)[4]
					process.get(element)[5]=process.get(element)[5]-process.get(element)[4]
					#print element,process.get(element)[5]
					#if(process.get(element)[5]==0):
						#io1.append(element)
						#print process.get(element)[3] 
						#process.get(element)[5]=ts
					#else:
					io.append(element)
					process.get(element)[3]=time+wt
					print process.get(element)[3]
					process.get(element)[4]=iotime
print RQ
